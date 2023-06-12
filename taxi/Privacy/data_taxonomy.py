from fideslang import DEFAULT_TAXONOMY
from fideslang.models import DataCategory,DataSubject,Dataset,DatasetCollection,DatasetField
from fideslang.manifests import write_manifest
import django
import sys
sys.path.append('../app')
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxi.settings')

django.setup()


import app.models as models
TAXONOMY = DEFAULT_TAXONOMY

TAXONOMY.data_category

new_data_categories=[DataCategory(
        fides_key="user.car_details",
        organization_fides_key="default_organization",
        name="User Data",
        description="Data related to the user's car. This information could be either car's color, car's model, car's brand or car's plate.",
        parent_key="user",
        is_default=True,
    ), DataCategory(
        fides_key="user.profile_photo",
        organization_fides_key="default_organization",
        name="User Data",
        description="A photograph of the user's face.",
        parent_key="user",
        is_default=True,
    ), DataCategory(
        fides_key="user.background",
        organization_fides_key="default_organization",
        name="User Data",
        description="Data related to the user's background. Including the criminal record and the license photograph.",
        parent_key="user",
        is_default=True,
    )]

new_data_subjects=[DataSubject(
            fides_key="palurdo_user",
            organization_fides_key="default_organization",
            name="Palurdo User",
            description="A PALURDO USER",
            is_default=True,
        ),]

TAXONOMY.data_category +=new_data_categories


## Este es un dataset de ejemplo. Utilicen las mismas clases (i.e Dataset, DatasetCollection, DatasetField) para armar su Dataset para la parte 3
v=Dataset(
            organization_fides_key=1,
            fides_key="test_sample_db_dataset",
            name="Sample DB Dataset",
            description="This is a Sample Database Dataset",
            data_categories=list(map(lambda x: x.fides_key,TAXONOMY.data_category)),
            collections=[
                DatasetCollection(
                    name="user",
                    fields=[
                        DatasetField(
                            name="Food_Preference",
                            description="User's favorite food",
                            retention="2 years"
                        ),
                        DatasetField(
                            name="First_Name",
                            description="A First Name Field",
                            data_categories=["user.name"],
                        ),
                        DatasetField(
                            name="Email",
                            description="User's Email",
                            data_categories=["user.contact.email"],
                        ),
                    ],
                )
            ],
        )
#write_manifest("data_classification.yaml",v.dict(exclude_none=True),"test")


def get_privacy_meta_data():
    models_list = [getattr(models, x) for x in dir(models) if isinstance(getattr(models, x), type)]
    privacy_meta_data={}
    for model in models_list:
        if hasattr(model,"PrivacyMeta"):
            privacy_meta_data[model.__name__]={}
            for attribute in model.PrivacyMeta.__dict__:
                if not attribute.startswith("__"):
                    privacy_meta_data[model.__name__][attribute]=model.PrivacyMeta.__dict__[attribute]
    return privacy_meta_data


def create_dataset():
    privacy_meta_data=get_privacy_meta_data()
    user_subjects={}
    for model_name in privacy_meta_data:
        for key in privacy_meta_data[model_name]:
            if "subject" in privacy_meta_data[model_name][key]:
                if privacy_meta_data[model_name][key]["subject"] is None:
                    continue
                if ',' in privacy_meta_data[model_name][key]["subject"]:
                    subject_list = privacy_meta_data[model_name][key]["subject"].split(',')
                    for subject2 in subject_list:
                        user_subjects[subject2]=[]
                else:
                    user_subjects[privacy_meta_data[model_name][key]["subject"]]=[]
    
    for subject in user_subjects:
        user_subjects[subject]=[]
        for model_name in privacy_meta_data:
            for key in privacy_meta_data[model_name]:
                if privacy_meta_data[model_name][key]["subject"] is None:
                    continue
                if subject in privacy_meta_data[model_name][key]["subject"]:
                    user_subjects[subject].append(DatasetField(
                                name=model_name,
                                description="",
                                retention=str(privacy_meta_data[model_name][key]["retention-time"]),
                                data_categories=[privacy_meta_data[model_name][key]["category"]],
                            ))

    for subject in user_subjects:
        user_subjects[subject]=DatasetCollection(
            name=subject,
            fields=user_subjects[subject],
        )
    dataset=Dataset(
        organization_fides_key=1,
        fides_key="privacy_db_dataset",
        name="Privacy Dataset",
        description="This is a Privacy Dataset for Taxi Company",
        data_categories=list(map(lambda x: x.fides_key,TAXONOMY.data_category)),
        collections=list(user_subjects.values()),
    )

    return dataset

dataset = create_dataset()
write_manifest("data_classification.yaml",dataset.dict(exclude_none=True),"")
