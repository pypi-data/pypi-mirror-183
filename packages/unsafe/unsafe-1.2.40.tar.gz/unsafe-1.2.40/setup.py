from setuptools import find_packages, setup

long_description = open('README.md', 'r').read()

requirements = [
    'requests<3.0,>=2.25.1',
    'PySocks==1.7.1',
    'beautifulsoup4==4.11.1',
    'Pillow==9.3.0',
    'urllib3==1.26.12'
]

setup(
    name='unsafe',
    version='1.2.40',
    author='Ahura Rahmani',
    author_email='ahur4.rahmani@gmail.com',
    maintainer='Masoud Nayebi',
    maintainer_email='mesut@gmail.com',
    license='MIT',
    url='https://github.com/ahur4/unsafe',
    install_requires=requirements,
    keywords=[
        'hack', 'hack-module', 'pentest', 'unsafe', 'osint',
        'osint-python', 'hacking-python', 'cryptography', 'vulnerability-scanner', 'vulnerability', 'security',
        'hacker', 'admin-finder', 'wordpress-scanner', 'instagram-osint', 'cve', 'proxy-wrapper', 'proxy-checker',
        'ssh-connect', 'hydra', 'cracker', 'sqlmap', 'ahur4', 'mesutfd','crawler','acunetix'
    ],
    description='A practical and optimal library for those interested in Pentest, cryptography,Vulnerability Scanner and ..',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={
        'face_recognition': ['utils/*.xml']
    },
    python_requires=">=3.8",
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
