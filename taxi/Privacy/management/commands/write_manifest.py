from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from fideslang.manifests import write_manifest
from Privacy.data_taxonomy import create_dataset 

class Command(BaseCommand):
    help = "Create a .yml file with the description of the dataset of PrivacyMeta"
    def handle(self, *args: Any, **options: Any):
        dataset = create_dataset()
        write_manifest("Privacy/data_classification.yaml",dataset.dict(exclude_none=True),"")
        self.stdout.write(self.style.SUCCESS('Manifest written successfully.'))