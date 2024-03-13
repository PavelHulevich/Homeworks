import random

from django.shortcuts import render

# Create your views here.


percentToggles = {
  "MyFeature": 80,
}


def IsEnable(toggleName: str) -> bool:
  percent = max(0, min(100, percentToggles[toggleName]))
  return percent >= random.randint(1, 100) + 1