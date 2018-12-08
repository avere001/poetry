from cleo.testers import CommandTester

from tests.helpers import get_package


def test_show_basic_with_installed_packages(app, poetry, installed):
    command = app.find("show")
    tester = CommandTester(command)

    cachy_010 = get_package("cachy", "0.1.0")
    cachy_010.description = "Cachy package"

    pendulum_200 = get_package("pendulum", "2.0.0")
    pendulum_200.description = "Pendulum package"

    pytest_373 = get_package("pytest", "3.7.3")
    pytest_373.description = "Pytest package"
    pytest_373.category = "dev"

    installed.add_package(cachy_010)
    installed.add_package(pendulum_200)
    installed.add_package(pytest_373)

    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.1.0",
                    "description": "Cachy package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
                {
                    "name": "pendulum",
                    "version": "2.0.0",
                    "description": "Pendulum package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
                {
                    "name": "pytest",
                    "version": "3.7.3",
                    "description": "Pytest package",
                    "category": "dev",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "pendulum": [], "pytest": []},
            },
        }
    )

    tester.execute()

    expected = """\
cachy    0.1.0 Cachy package
pendulum 2.0.0 Pendulum package
pytest   3.7.3 Pytest package
"""

    assert expected == tester.io.fetch_output()


def test_show_basic_with_not_installed_packages_non_decorated(app, poetry, installed):
    command = app.find("show")
    tester = CommandTester(command)

    cachy_010 = get_package("cachy", "0.1.0")
    cachy_010.description = "Cachy package"

    pendulum_200 = get_package("pendulum", "2.0.0")
    pendulum_200.description = "Pendulum package"

    installed.add_package(cachy_010)
    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.1.0",
                    "description": "Cachy package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
                {
                    "name": "pendulum",
                    "version": "2.0.0",
                    "description": "Pendulum package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "pendulum": []},
            },
        }
    )

    tester.execute()

    expected = """\
cachy        0.1.0 Cachy package
pendulum (!) 2.0.0 Pendulum package
"""

    assert expected == tester.io.fetch_output()


def test_show_basic_with_not_installed_packages_decorated(app, poetry, installed):
    command = app.find("show")
    tester = CommandTester(command)

    cachy_010 = get_package("cachy", "0.1.0")
    cachy_010.description = "Cachy package"

    pendulum_200 = get_package("pendulum", "2.0.0")
    pendulum_200.description = "Pendulum package"

    installed.add_package(cachy_010)
    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.1.0",
                    "description": "Cachy package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
                {
                    "name": "pendulum",
                    "version": "2.0.0",
                    "description": "Pendulum package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "pendulum": []},
            },
        }
    )

    tester.execute(decorated=True)

    expected = """\
\033[32mcachy   \033[0m \033[36m0.1.0\033[0m Cachy package
\033[31mpendulum\033[0m \033[36m2.0.0\033[0m Pendulum package
"""

    assert expected == tester.io.fetch_output()


def test_show_latest_non_decorated(app, poetry, installed, repo):
    command = app.find("show")
    tester = CommandTester(command)

    cachy_010 = get_package("cachy", "0.1.0")
    cachy_010.description = "Cachy package"
    cachy_020 = get_package("cachy", "0.2.0")
    cachy_020.description = "Cachy package"

    pendulum_200 = get_package("pendulum", "2.0.0")
    pendulum_200.description = "Pendulum package"
    pendulum_201 = get_package("pendulum", "2.0.1")
    pendulum_201.description = "Pendulum package"

    installed.add_package(cachy_010)
    installed.add_package(pendulum_200)

    repo.add_package(cachy_010)
    repo.add_package(cachy_020)
    repo.add_package(pendulum_200)
    repo.add_package(pendulum_201)

    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.1.0",
                    "description": "Cachy package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
                {
                    "name": "pendulum",
                    "version": "2.0.0",
                    "description": "Pendulum package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "pendulum": []},
            },
        }
    )

    tester.execute("--latest")

    expected = """\
cachy    0.1.0 0.2.0 Cachy package
pendulum 2.0.0 2.0.1 Pendulum package
"""

    assert expected == tester.io.fetch_output()


def test_show_latest_decorated(app, poetry, installed, repo):
    command = app.find("show")
    tester = CommandTester(command)

    cachy_010 = get_package("cachy", "0.1.0")
    cachy_010.description = "Cachy package"
    cachy_020 = get_package("cachy", "0.2.0")
    cachy_020.description = "Cachy package"

    pendulum_200 = get_package("pendulum", "2.0.0")
    pendulum_200.description = "Pendulum package"
    pendulum_201 = get_package("pendulum", "2.0.1")
    pendulum_201.description = "Pendulum package"

    installed.add_package(cachy_010)
    installed.add_package(pendulum_200)

    repo.add_package(cachy_010)
    repo.add_package(cachy_020)
    repo.add_package(pendulum_200)
    repo.add_package(pendulum_201)

    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.1.0",
                    "description": "Cachy package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
                {
                    "name": "pendulum",
                    "version": "2.0.0",
                    "description": "Pendulum package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "pendulum": []},
            },
        }
    )

    tester.execute("--latest", decorated=True)

    expected = """\
\033[32mcachy   \033[0m \033[36m0.1.0\033[0m \033[33m0.2.0\033[0m Cachy package
\033[32mpendulum\033[0m \033[36m2.0.0\033[0m \033[31m2.0.1\033[0m Pendulum package
"""

    assert expected == tester.io.fetch_output()


def test_show_outdated(app, poetry, installed, repo):
    command = app.find("show")
    tester = CommandTester(command)

    cachy_010 = get_package("cachy", "0.1.0")
    cachy_010.description = "Cachy package"
    cachy_020 = get_package("cachy", "0.2.0")
    cachy_020.description = "Cachy package"

    pendulum_200 = get_package("pendulum", "2.0.0")
    pendulum_200.description = "Pendulum package"

    installed.add_package(cachy_010)
    installed.add_package(pendulum_200)

    repo.add_package(cachy_010)
    repo.add_package(cachy_020)
    repo.add_package(pendulum_200)

    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.1.0",
                    "description": "Cachy package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
                {
                    "name": "pendulum",
                    "version": "2.0.0",
                    "description": "Pendulum package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "pendulum": []},
            },
        }
    )

    tester.execute("--outdated")

    expected = """\
cachy    0.1.0 0.2.0 Cachy package
"""

    assert expected == tester.io.fetch_output()


def test_show_hides_incompatible_package(app, poetry, installed, repo):
    command = app.find("show")
    tester = CommandTester(command)

    cachy_010 = get_package("cachy", "0.1.0")
    cachy_010.description = "Cachy package"

    pendulum_200 = get_package("pendulum", "2.0.0")
    pendulum_200.description = "Pendulum package"

    installed.add_package(pendulum_200)

    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.1.0",
                    "description": "Cachy package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                    "requirements": {"python": "1.0"},
                },
                {
                    "name": "pendulum",
                    "version": "2.0.0",
                    "description": "Pendulum package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "pendulum": []},
            },
        }
    )

    tester.execute()

    expected = """\
pendulum 2.0.0 Pendulum package
"""

    assert expected == tester.io.fetch_output()


def test_show_all_shows_incompatible_package(app, poetry, installed, repo):
    command = app.find("show")
    tester = CommandTester(command)

    cachy_010 = get_package("cachy", "0.1.0")
    cachy_010.description = "Cachy package"

    pendulum_200 = get_package("pendulum", "2.0.0")
    pendulum_200.description = "Pendulum package"

    installed.add_package(pendulum_200)

    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.1.0",
                    "description": "Cachy package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                    "requirements": {"python": "1.0"},
                },
                {
                    "name": "pendulum",
                    "version": "2.0.0",
                    "description": "Pendulum package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "pendulum": []},
            },
        }
    )

    tester.execute("--all")

    expected = """\
cachy     0.1.0 Cachy package
pendulum  2.0.0 Pendulum package
"""

    assert expected == tester.io.fetch_output()


def test_show_non_dev_with_basic_installed_packages(app, poetry, installed):
    command = app.find("show")
    tester = CommandTester(command)

    cachy_010 = get_package("cachy", "0.1.0")
    cachy_010.description = "Cachy package"

    pendulum_200 = get_package("pendulum", "2.0.0")
    pendulum_200.description = "Pendulum package"

    pytest_373 = get_package("pytest", "3.7.3")
    pytest_373.description = "Pytest package"
    pytest_373.category = "dev"

    installed.add_package(cachy_010)
    installed.add_package(pendulum_200)
    installed.add_package(pytest_373)

    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.1.0",
                    "description": "Cachy package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
                {
                    "name": "pendulum",
                    "version": "2.0.0",
                    "description": "Pendulum package",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
                {
                    "name": "pytest",
                    "version": "3.7.3",
                    "description": "Pytest package",
                    "category": "dev",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "pendulum": [], "pytest": []},
            },
        }
    )

    tester.execute("--no-dev")

    expected = """\
cachy    0.1.0 Cachy package
pendulum 2.0.0 Pendulum package
"""

    assert expected == tester.io.fetch_output()


def test_show_tree(app, poetry, installed):
    command = app.find("show")
    tester = CommandTester(command)

    poetry.package.add_dependency("cachy", "^0.2.0")

    cachy2 = get_package("cachy", "0.2.0")
    cachy2.add_dependency("msgpack-python", ">=0.5 <0.6")

    installed.add_package(cachy2)

    poetry.locker.mock_lock_data(
        {
            "package": [
                {
                    "name": "cachy",
                    "version": "0.2.0",
                    "description": "",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                    "dependencies": {"msgpack-python": ">=0.5 <0.6"},
                },
                {
                    "name": "msgpack-python",
                    "version": "0.5.1",
                    "description": "",
                    "category": "main",
                    "optional": False,
                    "platform": "*",
                    "python-versions": "*",
                    "checksum": [],
                },
            ],
            "metadata": {
                "python-versions": "*",
                "platform": "*",
                "content-hash": "123456789",
                "hashes": {"cachy": [], "msgpack-python": []},
            },
        }
    )

    tester.execute("--tree")

    expected = """\
cachy 0.2.0
`-- msgpack-python >=0.5 <0.6
"""

    assert expected == tester.io.fetch_output()
