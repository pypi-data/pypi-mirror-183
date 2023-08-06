# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['psod', 'psod.outlier_detection']

package_data = \
{'': ['*']}

install_requires = \
['category_encoders>=2.3.0',
 'numpy>=1.19.4,<2.0.0',
 'pandas>=1.1.5,<2.0.0',
 'scikit-learn>=1.0.1,<2.0.0',
 'tqdm>=4.00.0,<5.0.0']

setup_kwargs = {
    'name': 'psod',
    'version': '0.0.3',
    'description': 'Outlier detection using supervised methods in a supervised context',
    'long_description': '# Pseudo-supervised outlier detection\n\n> A highly performant alternative to purely unsupervised approaches.\n\nPSOD uses supervised methods to identify outliers in unsupervised contexts. It offers higher accuracy for outliers\nwith top scores than other models while keeping comparable performance on the whole dataset.\n\nThe usage is simple.\n\n1.) Install the package:\n```sh\npip install psod\n```\n\n2.) Import the package:\n```sh\nfrom psod.outlier_detection.psod import PSOD\n```\n\n3.) Instantiate the class:\n```sh\niso_class = PSOD()\n```\nThe class has multiple arguments that can be passed. If older labels exist these could be used\nfor hyperparameter tuning.\n\n4.) Recommended: Normalize the data\n```sh\nfrom sklearn.preprocessing import MinMaxScaler\nscaler = MinMaxScaler()\nscaler.fit(treatment_data[cols])\nscaled = scaler.transform(treatment_data[cols])\nscaled = pd.DataFrame(scaled, columns=cols)\n```\n\n5.) Fit and predict:\n```sh\nfull_res = iso_class.fit_predict(scaled, return_class=True)\n```\n\n6.) Predict on new data:\n```sh\nfull_res = iso_class.predict(scaled, return_class=True)\n```\n\nClasses and outlier scores can always be accessed from the class instance via:\n```sh\niso_class.scores  # getting the outlier scores\niso_class.outlier_classes  # get the classes\n```\n\nThe repo contains example notebooks. Please note that example notebooks do not always contain the newest version. \nThe file psod.py is always the most updated one.\n[See the full article](https://medium.com/@thomasmeissnerds)\n\n\n## Meta\n\nCreator: Thomas Meißner – [LinkedIn](https://www.linkedin.com/in/thomas-mei%C3%9Fner-m-a-3808b346)\n\n[PSOD GitHub repository](https://github.com/ThomasMeissnerDS/PSOD)',
    'author': 'Thomas Meißner',
    'author_email': 'meissnercorporation@gmx.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ThomasMeissnerDS/PSOD',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<=3.10',
}


setup(**setup_kwargs)
