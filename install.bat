@echo off

echo clone models
git lfs install
git clone https://huggingface.co/fudan-generative-ai/hallo pretrained_models

echo Install Depends
python -m venv venv
call venv/scripts/activate
pip install -r requerements.txt
pip install -e . 

pip install bitsandbytes-windows --force-reinstall

echo Install GPU libs
pip install torch==2.2.2+cu121 torchaudio torchvision --index-url https://download.pytorch.org/whl/cu121
pip install onnxruntime-gpu

echo install complete
pause