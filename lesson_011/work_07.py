# Для Linux есть проект -pyenv https://github.com/pyenv/pyenv
# git clone https://github.com/pyenv/pyenv.git ~/.pyenv
# клонируется в папку .pyenv в домашней деректории
# $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
# $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
# $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
# я заменил bash_profile на bashrc - особенности Linux Nint
# и установим пакеты ОС необходимые для сборки пайтона (https://github.com/pyenv/pyenv/wiki)
# $ sudo apt-get install -y make build-essential libssl-dev zliblg-dev libbz2-dev libreadline-dev
# $ sudo apt-get install -y libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev
# $ sudo apt-get install -y libxmlsec1-dev libffi-dev
# далее перегружаем консоль и вводим команды pyenv
# $ pyenv versions
# $ pyenv install 3.6.1
# pyenv скачивает исходники и компилит нужную версию пайтона, распологаться она будет в
# $ ls -al ~/.pyenv/versions
