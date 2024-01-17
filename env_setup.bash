ve() {
    local py=${1:-python3.8}
    local venv="${2:-./.venv}"

    local bin="${venv}/bin/activate"

	  if [ -z "${VIRTUAL_ENV}" ]; then
        if [ ! -d ${venv} ]; then
            echo "virtualenv ${venv} - creating & activating"
            ${py} -m venv ${venv} --system-site-package
            echo "export PYTHON=${py}" >> ${bin} # overwrite
            source ${bin}
            echo "Upgrading pip"
            ${py} -m pip install --upgrade pip
        else
            echo "virtualenv ${venv} - exists :. activating"
            source ${bin}
        fi
    else
        echo "virtualenv - already activated"
    fi
}