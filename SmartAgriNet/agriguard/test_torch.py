try:
    import torch
    print(f"PyTorch version: {torch.__version__}")
    print("CUDA available:", torch.cuda.is_available())
    print("Torch installed successfully!")
except ImportError as e:
    print(f"Torch not installed: {e}")
