# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['convert_labse_tf_pt']

package_data = \
{'': ['*'], 'convert_labse_tf_pt': ['data/smaller_vocab/*']}

install_requires = \
['ipywidgets>=7.6.3,<8.0.0',
 'loguru>=0.6.0,<0.7.0',
 'tensorflow-hub>=0.12.0,<0.13.0',
 'transformers[flax,sentencepiece,tf,torch]>=4.22.0,<5.0.0']

entry_points = \
{'console_scripts': ['convert_labse = convert_labse_tf_pt.convert:main']}

setup_kwargs = {
    'name': 'convert-labse-tf-pt',
    'version': '2.0.0',
    'description': 'Convert LaBSE model from TensorFlow to PyTorch.',
    'long_description': "# LaBSE\n\n## Project\n\nThis project is an implementation to convert Google's [LaBSE](https://tfhub.dev/google/LaBSE/2) model from TensorFlow to PyTorch. It also offers extensions to convert the [smaller-LaBSE model](https://tfhub.dev/jeongukjae/smaller_LaBSE_15lang/1) from TensorFlow to PyTorch.\n\nThe models are uploaded to the [HuggingFace Model Hub](https://huggingface.co/setu4993/) in the PyTorch, HF-compatible TensorFlow and Flax formats, alongwith a compatible tokenizer.\n\n- [LaBSE](https://huggingface.co/setu4993/LaBSE)\n- [smaller-LaBSE](https://huggingface.co/setu4993/smaller-LaBSE)\n\n## Model Cards\n\nSee the [`model-cards` directory](https://github.com/setu4993/convert-labse-tf-pt/tree/main/model-cards) for a copy of the model cards.\n\n## License\n\nThis repository and the conversion code is licensed under the MIT license, but the **model** is distributed with an Apache-2.0 license.\n",
    'author': 'Setu Shah',
    'author_email': 'setu+labse@setu.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/setu4993/convert-labse-tf-pt',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
