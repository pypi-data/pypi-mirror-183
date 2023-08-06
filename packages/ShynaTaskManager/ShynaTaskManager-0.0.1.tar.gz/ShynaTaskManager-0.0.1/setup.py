from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name='ShynaTaskManager',
    version='0.0.1',
    packages=find_packages(),
    author="Shivam Sharma",
    author_email="shivamsharma1913@gmail.com",
    description="Shyna Task Manager, Phase one",
    long_description=long_description,
    long_description_content_type="text/markdown",
)

install_requires = ['ShynaTime', 'ShynaDatabase', 'ShynaTelegramBotNotification', 'nltk', 'sox', 'setuptools', 'wheel',
                    'google_speech','Shyna_speaks', 'python-telegram-bot', 'shynais', 'Chatterbot==1.0.4', 'ShynaJokes',
                    'mediawikiapi', 'ShynaGreetings', 'ShynaWeather']

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
