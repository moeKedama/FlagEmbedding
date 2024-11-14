from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='FlagEmbedding',
    version='1.3.2',
    description='FlagEmbedding',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='2906698981@qq.com',
    url='https://github.com/FlagOpen/FlagEmbedding',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch>=1.6.0',
        'transformers~=4.45.1',
        'datasets',
        'accelerate>=0.20.1',
        'peft',
        'ir-datasets',
        'sentencepiece',
        'protobuf',
        'gradio'~=5.4.0,
        'openai'==1.38.0,
        'nltk'~=3.9.1,
        'scikit-learn'~=1.5.2,
        'fire'~=0.5.0,
        'autofaiss'~=2.17.0,
        'llama-recipes'==0.0.3,
        'grpcio'==1.62.1,
        'grpcio-tools'==1.62.1,
        'protobuf'==4.25.3,
        'sentence-transformers,
    ],
    extras_require={
        'finetune': ['deepspeed', 'flash-attn'],
    },
)
