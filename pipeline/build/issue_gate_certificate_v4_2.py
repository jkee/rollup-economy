#!/usr/bin/env python3
"""Issue a v4.2 regression/holdout certificate from an accepted exact gate."""

import importlib.util
import os


HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


campaign = _load("campaign_v4_2_for_gate_issuer", "campaign_v4_2.py")
implementation = _load("gate_certificate_v4_2_implementation", "issue_gate_certificate_v4_1.py")
implementation.campaign = campaign

CertificateError = implementation.CertificateError
issue = implementation.issue


def main(argv=None):
    return implementation.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
