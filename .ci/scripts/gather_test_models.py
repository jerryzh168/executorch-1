#!/usr/bin/env python

import json
import os
from typing import Any

from examples.models import MODEL_NAME_TO_MODEL


def set_output(name: str, val: Any) -> None:
    """
    Set the GitHb output so that it can be accessed by other jobs
    """
    print(f"Setting {val} to GitHub output")

    if os.getenv("GITHUB_OUTPUT"):
        with open(str(os.getenv("GITHUB_OUTPUT")), "a") as env:
            print(f"{name}={val}", file=env)
    else:
        print(f"::set-output name={name}::{val}")


def export_models_for_ci() -> None:
    """
    This gathers all the example models that we want to test on GitHub OSS CI
    """
    # This is the JSON syntax for configuration matrix used by GitHub
    # https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs
    models = {"include": [{"model": name} for name in MODEL_NAME_TO_MODEL.keys()]}
    set_output("models", json.dumps(models))


if __name__ == "__main__":
    export_models_for_ci()
