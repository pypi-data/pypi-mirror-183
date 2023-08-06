from setuptools import setup, find_packages
setup(
    name = 'ingl',
    version = '0.0.301',
    description = "A command line interface for interacting with Ingl-DAO Program Instructions",
    author = 'Ingl',
    author_email = 'admin@ingl.io',
    url = 'https://www.ingl.io',
    packages = find_packages(),
    install_requires = [
        'asyncclick',
        'Click',
        'solana',
        'borsh_construct',
        'base58',
        'rich',
        'ledgerblue',
        ],
    entry_points = '''
    [console_scripts]
    ingl=src.ingl_cli:entry
    '''
)