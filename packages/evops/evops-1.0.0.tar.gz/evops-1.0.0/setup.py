# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['evops', 'evops.benchmark', 'evops.metrics', 'evops.utils']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=4.8.3,<5.0.0',
 'importlib-resources>=5.7.1,<6.0.0',
 'nptyping>=1.4.4,<2.0.0',
 'numpy>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'evops',
    'version': '1.0.0',
    'description': 'Evaluation of Plane Segmentation.',
    'long_description': '<p style="text-align:center">\n    <img src="./docs/_static/logo.png" width="250" height="250"/>\n</p>\n\n# EVOPS: library for evaluating plane segmentation algorithms\n[![Build and publish](https://github.com/Perception-Solutions/evops/actions/workflows/ci.yml/badge.svg)](https://github.com/Perception-Solutions/evops/actions/workflows/ci.yml)\n\n<p style="font-size: 14pt;">\n     EVOPS is an open-source python library that provides various metrics for evaluating the results of the algorithms for segmenting and associating planes from point clouds collected from LIDARs and RGBD devices. \n</p>\n\n<p style="font-size: 14pt;">\n     List of metrics implemented in the library:\n</p>\n\n<ul style="font-size: 14pt;">\n    <li>Summary segmentation metrics <ul style="font-size: 14pt;">\n        <li><a href="https://prime-slam.github.io/evops-metrics/instance_based/panoptic">Panoptic</a></li>\n        <li><a href="https://prime-slam.github.io/evops-metrics/full_statistics/full_statistics">Full statistics</a></li>\n    </ul></li>\n    <li>Instance-based segmentation metrics\n        <ul style="font-size: 14pt;">\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/instance_based/precision">Precision</a></li>\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/instance_based/recall">Recall</a></li>\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/instance_based/fScore">F-Score</a></li>\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/instance_based/usr">Under segmented ratio</a></li>\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/instance_based/osr">Over segmented ratio</a></li>\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/instance_based/noise">Noise ratio</a></li>\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/instance_based/missed">Missed ratio</a></li>\n    </ul></li>\n    <li>Point-based segmentation metrics\n        <ul style="font-size: 14pt;">\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/point_based/iou">Intersection over Union (IoU)</a></li>\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/point_based/dice">Dice</a></li>\n            <li><a href="https://prime-slam.github.io/evops-metrics/#/metrics/point_based/mean">Mean of some metric for matched instances</a></li>\n    </ul></li>\n</ul>\n\n<p style="font-size: 14pt;">\n    For more, please visit the <a href="https://prime-slam.github.io/evops-metrics">EVOPS documentation</a>.\n</p>\n<p style="font-size: 14pt;">\n    You can also find full information about the project on the <a href="https://evops.netlify.app/">EVOPS project website</a>.\n</p>\n\n# Python quick start\n\n<p style="font-size: 14pt;">\n     Library can be installed using the pip package manager:\n</p>\n\n```bash\n$ # Install package\n$ pip install evops\n\n$ # Check installed version of package\n$ pip show evops\n```\n\n# Example of usage\n\n<p style="font-size: 14pt;">\n    Below is an example of using the precision metric:\n</p>\n\n```bash\n>>> from evops.metrics import precision\n>>> pred_labels = np.array([1, 1, 3, 3])\n>>> gt_labels = np.array([2, 2, 0, 3])\n>>> tp_condition = "iou"\n>>> precision(pred_labels, gt_labels, tp_condition)\n0.5\n```\n\n# Citation\n```\n@misc{kornilova2022evops,\n      title={EVOPS Benchmark: Evaluation of Plane Segmentation from RGBD and LiDAR Data}, \n      author={Anastasiia Kornilova, Dmitrii Iarosh, Denis Kukushkin, Nikolai Goncharov, Pavel Mokeev, Arthur Saliou, Gonzalo Ferrer},\n      year={2022},\n      eprint={2204.05799},\n      archivePrefix={arXiv},\n      primaryClass={cs.CV}\n}\n```\n\n# License\n\n<p style="font-size: 14pt;">\n    This project is licensed under the Apache License - see the <a href="https://github.com/Perception-Solutions/evops/blob/main/LICENSE">LICENSE</a> file for details.\n</p>',
    'author': 'Pavel Mokeev',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://evops.netlify.app/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
