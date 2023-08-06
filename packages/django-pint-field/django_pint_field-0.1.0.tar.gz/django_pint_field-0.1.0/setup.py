# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_pint_field', 'django_pint_field.migrations']

package_data = \
{'': ['*']}

install_requires = \
['django-extensions>=3.2.1,<4.0.0',
 'django>=4.1.4,<5.0.0',
 'pint>=0.20.1,<0.21.0',
 'psycopg2-binary>=2.9.5,<3.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'pytest>=7.2.0,<8.0.0',
 'werkzeug>=2.2.2,<3.0.0']

setup_kwargs = {
    'name': 'django-pint-field',
    'version': '0.1.0',
    'description': 'Pint Fields for Django and Postgres',
    'long_description': '# django-pint-field\n\nUse pint with Django\'s ORM\n\nModified from the fantastic [django-pint](https://github.com/CarliJoy/django-pint) with different goals.\n\nUnlike django-pint, in this project we use a composite field to store both the magnitude and value of the field, along with the equivalent value in base units for lookups. For this reason, the project only works with Postgresql databases. It ensures that the units your users want to use are the units they see, while still allowing accurate comparisons of one quantity to another.\n\n## Install\n\n`pip install django_pint_field`\n\n\n## Usage\n\n```python\nfrom decimal import Decimal\nfrom django_pint_field.units import ureg\nQuantity = ureg.Quantity\n\n# Start by creating a few Pint Quantity objects\nextra_small = Quantity(1 * ureg.gram)\nsmall = Quantity(10 * ureg.gram)\nmedium = Quantity(100 * ureg.gram)\nlarge = Quantity(1000 * ureg.gram)\nextra_large = Quantity(10000 * ureg.gram)\n\n# Create a couple objects\nIntegerPintFieldSaveModel.objects.create(name="small", weight=small)\nIntegerPintFieldSaveModel.objects.create(name="large", weight=large)\n\n# Perform some queries\nIntegerPintFieldSaveModel.objects.filter(weight__gt=medium)\n<QuerySet [<IntegerPintFieldSaveModel: large>]>\n\nIntegerPintFieldSaveModel.objects.filter(weight__gt=extra_small)\n<QuerySet [<IntegerPintFieldSaveModel: small>, <IntegerPintFieldSaveModel: large>]>\n\nIntegerPintFieldSaveModel.objects.filter(weight__gte=small)\n<QuerySet [<IntegerPintFieldSaveModel: small>, <IntegerPintFieldSaveModel: large>]>\n\nIntegerPintFieldSaveModel.objects.filter(weight__range=(small, medium))\n<QuerySet [<IntegerPintFieldSaveModel: small>]>\n```\n\n## Valid Lookups\n\nOther lookups will be added in the future. Currently available are:\n\n- exact\n- iexact\n- gt\n- gte\n- lt\n- lte\n- range\n- isnull\n\n## Creating your own units\n\n*Will be detailed soon*\n\n\n## Model Fields\n\n- **IntegerPintField**: Stores a pint measurement as an integer (-2147483648 to 2147483647).\n- **BigIntegerPintField**: Stores a pint measurement as a big integer (-9223372036854775808 to 9223372036854775807).\n- **DecimalPintField**: Stores a pint measurement as a decimal.\n\n## Form Fields\n\n- **IntegerPintFormField**: Used in forms with IntegerPintField and BigIntegerPintField.\n- **DecimalPintFormField**: Used in forms with DecimalPintField.\n\n## Widgets\n\n- **PintFieldWidget**: Default widget for all django pint field types.\n\n\n## Settings\n\n<dl>\n  <dt><code>DJANGO_PINT_FIELD_DECIMAL_PRECISION</code></dt>\n  <dd>\n    Determines whether django_pint_field should automatically set the python decimal precision for the project. If an integer greater than 0 is provided, the decimal context precision for the entire project will be set to that value. Otherwise, the precision remains at the default (usually 28).<br>\n    <em>* Type: int</em>\n    <em>* Default: 0</em>\n  </dd>\n</dl>\n\n\n## Rounding modes (upcoming feature)\n\n**decimal.ROUND_CEILING**\nRound towards Infinity.\n\n**decimal.ROUND_DOWN**\nRound towards zero.\n\n**decimal.ROUND_FLOOR**\nRound towards -Infinity.\n\n**decimal.ROUND_HALF_DOWN**\nRound to nearest with ties going towards zero.\n\n**decimal.ROUND_HALF_EVEN**\nRound to nearest with ties going to nearest even integer.\n\n**decimal.ROUND_HALF_UP**\nRound to nearest with ties going away from zero.\n\n**decimal.ROUND_UP**\nRound away from zero.\n\n**decimal.ROUND_05UP**\nRound away from zero if last digit after rounding towards zero would have been 0 or 5; otherwise round towards zero.\n\nRead more about rounding modes for decimals at the [decimal docs](https://docs.python.org/3/library/decimal.html#rounding-modes)\n\n\n\n## Use the test app with docker compose\n\n### Build and bring up\n\n```\ndocker compose build\ndocker compose run django python manage.py migrate\ndocker compose run django python manage.py createsuperuser\ndocker compose up -d\n```\n\nNavigate to `127.0.0.1:8000`\n\n### Test (assuming you have already performed `build`)\n\n`docker compose run django python manage.py test`\n\n## Run psql on the Postgres database\n\n`docker compose exec postgres psql -U postgres`\n\n\n## ToDos:\n- If a unit_choices value is an alias (e.g. pounds vs pound), the form widget will show the incorrect item selected. The correct value is saved in db, though.\n- Implement rounding modes\n- ',
    'author': 'Jack Linke',
    'author_email': 'jack@watervize.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jacklinke/django-pint-field',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
