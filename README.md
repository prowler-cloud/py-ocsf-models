# py-ocsf-models

The `py-ocsf-models` package offers a Python implementation of the Open Cybersecurity Schema Framework (OCSF) models, facilitating the manipulation and understanding of cybersecurity data within Python applications. This package provides a rich set of models covering various aspects of cybersecurity events, findings, objects, and profiles as defined by the OCSF Schema, enabling developers to work with structured cybersecurity data efficiently.

In [Prowler](https://github.com/prowler-cloud/prowler), we leverage the py-ocsf-models package to generate JSON formatted OCSF outputs, specifically focusing on Detection Findings. This integration facilitates the standardization and sharing of cybersecurity findings in a structured and widely-accepted format, enhancing the interoperability between different security tools and platforms.

## Features

- **Comprehensive OCSF Schema Implementation**: Includes models for events, findings, objects, and profiles, covering the entire OCSF Schema.
- **Easy Data Manipulation**: Easily create, modify, and interact with cybersecurity data structures.
- **Serialization and Deserialization Support**: Convert OCSF model instances to and from JSON for easy storage and transmission.
- **Extensible Design**: Extend and customize models to fit specific requirements while staying compliant with the OCSF schema.

## OCSF Coverage

- Detection Finding
- Compliance Finding
- Application Security Posture Finding

## Installation

Install `py-ocsf-models` using pip:

```bash
pip install py-ocsf-models
```

Import the package in your Python application:

```python
import py_ocsf_models
```

## Usage Examples

You can find ready-to-run examples demonstrating how to generate events using the OCSF schema in the [examples](./examples/) folder.

## How to Release

To release a new version of `py-ocsf-models`:

1. **Create a PR with version update**: Update the version number in `pyproject.toml` and create a pull request with the changes.

2. **Create a GitHub release**: Once the PR is merged into the master branch, create a new release in GitHub from the master branch. This will automatically trigger the `pypi-release.yml` workflow to publish the package to PyPI.

## Contributing
Contributions are welcome! Whether you're fixing a bug, adding new features, or improving the documentation, please feel free to make a pull request or open an issue.

## License
This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
This package is built to support and encourage the adoption of the Open Cybersecurity Schema Framework (OCSF) and facilitate the handling of cybersecurity data in Python applications.

## Support
For support, questions, or feedback, please open an issue on the GitHub repository.
