# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['abcdrl']

package_data = \
{'': ['*']}

install_requires = \
['combine_signatures>=0.1.0,<0.2.0',
 'dill>=0.3.6,<0.4.0',
 'fire>=0.5.0,<0.6.0',
 'gymnasium>=0.27.0,<0.28.0',
 'moviepy>=1.0.0',
 'opencv-python>=3.0',
 'pygame==2.1.3.dev8',
 'tensorboard>=2.10.0,<3.0.0',
 'wandb>=0.13.7,<0.14.0']

extras_require = \
{'all': ['torch>=1.12.1,<2.0.0',
         'shimmy[atari]>=0.1.0,<1.0',
         'autorom[accept-rom-license]>=0.4.2,<0.5.0',
         'mujoco>=2.3.1.post1',
         'mujoco-py>=2.1,<2.2',
         'imageio>=2.14.1',
         'free-mujoco-py==2.1.6'],
 'atari': ['shimmy[atari]>=0.1.0,<1.0',
           'autorom[accept-rom-license]>=0.4.2,<0.5.0'],
 'mujoco': ['mujoco>=2.3.1.post1',
            'mujoco-py>=2.1,<2.2',
            'imageio>=2.14.1',
            'free-mujoco-py==2.1.6'],
 'torch': ['torch>=1.12.1,<2.0.0']}

setup_kwargs = {
    'name': 'abcdrl',
    'version': '0.2.0a4',
    'description': 'Modular Single-file Reinfocement Learning Algorithms Library',
    'long_description': '# **abcdRL** (Implement a RL algorithm in four simple steps)\n\nEnglish | [简体中文](./README.cn.md)\n\n[![license](https://img.shields.io/pypi/l/abcdrl)](https://github.com/sdpkjc/abcdrl)\n[![pytest](https://github.com/sdpkjc/abcdrl/actions/workflows/test.yml/badge.svg)](https://github.com/sdpkjc/abcdrl/actions/workflows/test.yml)\n[![pre-commit](https://github.com/sdpkjc/abcdrl/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/sdpkjc/abcdrl/actions/workflows/pre-commit.yml)\n[![pypi](https://img.shields.io/pypi/v/abcdrl)](https://pypi.org/project/abcdrl)\n[![docker autobuild](https://img.shields.io/docker/cloud/build/sdpkjc/abcdrl)](https://hub.docker.com/r/sdpkjc/abcdrl/)\n[![docs](https://img.shields.io/github/deployments/sdpkjc/abcdrl/Production?label=docs&logo=vercel)](https://docs.abcdrl.xyz/)\n[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/sdpkjc/abcdrl)\n[![benchmark](https://img.shields.io/badge/Weights%20&%20Biases-benchmark-FFBE00?logo=weightsandbiases)](https://report.abcdrl.xyz/)\n[![mirror repo](https://img.shields.io/badge/Gitee-mirror%20repo-black?style=flat&labelColor=C71D23&logo=gitee)](https://gitee.com/sdpkjc/abcdrl/)\n[![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue)](http://mypy-lang.org/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n[![python versions](https://img.shields.io/pypi/pyversions/abcdrl)](https://pypi.org/project/abcdrl)\n\nabcdRL is a **Modular Single-file Reinforcement Learning Algorithms Library** that provides modular design without strict and clean single-file implementation.\n\n<img src="https://abcdrl.xyz/logo/adam.svg" width="300"/>\n\n*When reading the code, understand the full implementation details of the algorithm in the single file quickly; When modifying the algorithm, benefiting from a lightweight modular design, only need to focus on a small number of modules.*\n\n> abcdRL mainly references the single-file design philosophy of [vwxyzjn/cleanrl](https://github.com/vwxyzjn/cleanrl/) and the module design of [PaddlePaddle/PARL](https://github.com/PaddlePaddle/PARL/).\n\n***Documentation ➡️ [docs.abcdrl.xyz](https://abcdrl.xyz)***\n\n***Roadmap🗺️ [#57](https://github.com/sdpkjc/abcdrl/issues/57)***\n\n## 🚀 Quickstart\n\nOpen the project in Gitpod🌐 and start coding immediately.\n\n[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/sdpkjc/abcdrl)\n\nUsing Docker📦:\n\n```bash\n# 0. Prerequisites: Docker & Nvidia Drive & NVIDIA Container Toolkit\n# 1. Run DQN algorithm\ndocker run --rm --gpus all sdpkjc/abcdrl python abcdrl/dqn.py\n```\n\n***[For detailed installation instructions 👀](https://docs.abcdrl.xyz/install/)***\n\n## 🐼 Features\n\n- 👨\u200d👩\u200d👧\u200d👦 Unified code structure\n- 📄 Single-file implementation\n- 🐷 Low code reuse\n- 📐 Minimizing code differences\n- 📈 Tensorboard & Wandb support\n- 🛤 PEP8(code style) & PEP526(type hint) compliant\n\n## 🗽 Design Philosophy\n\n- "Copy📋", ~~not "Inheritance🧬"~~\n- "Single-file📜", ~~not "Multi-file📚"~~\n- "Features reuse🛠", ~~not "Algorithms reuse🖨"~~\n- "Unified logic🤖", ~~not "Unified interface🔌"~~\n\n## ✅ Implemented Algorithms\n\n***Weights & Biases Benchmark Report ➡️ [report.abcdrl.xyz](https://report.abcdrl.xyz)***\n\n- [Deep Q Network (DQN)](https://doi.org/10.1038/nature14236)\n- [Deep Deterministic Policy Gradient (DDPG)](http://arxiv.org/abs/1509.02971)\n- [Twin Delayed Deep Deterministic Policy Gradient (TD3)](http://arxiv.org/abs/1802.09477)\n- [Soft Actor-Critic (SAC)](http://arxiv.org/abs/1801.01290)\n- [Proximal Policy Optimization (PPO)](http://arxiv.org/abs/1802.09477)\n\n---\n\n- [Double Deep Q Network (DDQN)](http://arxiv.org/abs/1509.06461)\n- [Prioritized Deep Q Network (PDQN)](http://arxiv.org/abs/1511.05952)\n\n## Citing abcdRL\n\n```bibtex\n@misc{zhao_abcdrl_2022,\n    author = {Yanxiao, Zhao},\n    month = {12},\n    title = {{abcdRL: Modular Single-file Reinforcement Learning Algorithms Library}},\n    url = {https://github.com/sdpkjc/abcdrl},\n    year = {2022}\n}\n```\n',
    'author': 'Adam Zhao',
    'author_email': 'pazyx728@gmail.com',
    'maintainer': 'Adam Zhao',
    'maintainer_email': 'pazyx728@gmail.com',
    'url': 'https://abcdrl.xyz/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
