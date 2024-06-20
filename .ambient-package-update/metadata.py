from ambient_package_update.metadata.author import PackageAuthor
from ambient_package_update.metadata.constants import (
    DEV_DEPENDENCIES,
    LICENSE_GPL,
    SUPPORTED_DJANGO_VERSIONS,
    SUPPORTED_PYTHON_VERSIONS,
)
from ambient_package_update.metadata.maintainer import PackageMaintainer
from ambient_package_update.metadata.package import PackageMetadata
from ambient_package_update.metadata.readme import ReadmeContent
from ambient_package_update.metadata.ruff_ignored_inspection import RuffIgnoredInspection

METADATA = PackageMetadata(
    package_name="django_pony_express",
    module_name="django_pony_express",
    authors=[
        PackageAuthor(
            name="Ambient Digital",
            email="hello@ambient.digital",
        ),
    ],
    maintainer=PackageMaintainer(name="Ambient Digital", url="https://ambient.digital/", email="hello@ambient.digital"),
    company="Ambient Innovation: GmbH",
    license=LICENSE_GPL,
    license_year=2023,
    development_status="5 - Production/Stable",
    has_migrations=False,
    readme_content=ReadmeContent(uses_internationalisation=True),
    dependencies=[
        "Django>=3.2",
        "html2text>=2020.1.16",
    ],
    supported_django_versions=SUPPORTED_DJANGO_VERSIONS,
    supported_python_versions=SUPPORTED_PYTHON_VERSIONS,
    optional_dependencies={
        "dev": [
            *DEV_DEPENDENCIES,
        ],
    },
    ruff_ignore_list=[
        RuffIgnoredInspection(key="N999", comment="Project name contains underscore, not fixable"),
        RuffIgnoredInspection(key="A003", comment="Django attributes shadow python builtins"),
        RuffIgnoredInspection(key="DJ001", comment="Django model text-based fields shouldn't be nullable"),
        RuffIgnoredInspection(key="B905", comment="Can be enabled when Python <=3.9 support is dropped"),
    ],
)
