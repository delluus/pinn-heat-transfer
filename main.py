def main():
    print("Hello from pinn-heat-transfer!")

    # print some torch and numpy info
    import torch
    import numpy as np

    print(torch.__version__)
    print(np.__version__)
    print(torch.cuda.is_available())
    print(torch.cuda.get_device_name(0))


if __name__ == "__main__":
    main()
