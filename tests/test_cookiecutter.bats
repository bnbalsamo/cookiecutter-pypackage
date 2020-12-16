#!/usr/bin/env bats

@test "end to end" {
    # Install Deps
    set -xe
    cookiecutter . --no-input
    # Commands which appears in post hook
    [[ `type -t pyenv` ]]
    [ -s "$PYENV_ROOT/plugins/pyenv-virtualenv" ]
    [ -s "$PYENV_ROOT/plugins/xxenv-latest" ]
    PROJECT_NAME="MyProject"
    pyenv latest install -s 3.8
    PYENV_LATEST_38=$(pyenv latest -p 3.8)
    pyenv latest install -s 3.7
    PYENV_LATEST_37=$(pyenv latest -p 3.7)
    pyenv latest install -s 3.6
    PYENV_LATEST_36=$(pyenv latest -p 3.6)
    cd $PROJECT_NAME
    git init
    git add {.[!.]*,*}
    git commit -m "first commit"
    # Omitting push to git remote
    pyenv virtualenv "$PYENV_LATEST_38" "$PROJECT_NAME"
    pyenv local "$PROJECT_NAME" "$PYENV_LATEST_38" "$PYENV_LATEST_37" "$PYENV_LATEST_36"
    pip install -r "requirements/requirements_dev.txt
    inv run.tests
}
