import platform
from unittest import mock

import pytest
import torch

try:
    from nvidia.dali import ops, types, pipeline, plugin
except (ImportError, ModuleNotFoundError):
    DALI_AVAILABLE = False
else:
    DALI_AVAILABLE = True

dp_16_args = """
--max_epochs 1 \
--batch_size 32 \
--limit_train_batches 2 \
--limit_val_batches 2 \
--gpus 2 \
--distributed_backend dp \
--precision 16 \
"""

cpu_args = """
--max_epochs 1 \
--batch_size 32 \
--limit_train_batches 2 \
--limit_val_batches 2 \
"""

ddp_args = """
--max_epochs 1 \
--batch_size 32 \
--limit_train_batches 2 \
--limit_val_batches 2 \
--gpus 2 \
--precision 16 \
"""

# TODO
# @pytest.mark.skipif(torch.cuda.device_count() < 2, reason="test requires multi-GPU machine")
# @pytest.mark.parametrize('cli_args', [dp_16_args])
# def test_examples_dp_mnist(cli_args):
#     from pl_examples.basic_examples.mnist import cli_main
#
#     with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
#         cli_main()


# TODO
# @pytest.mark.skipif(torch.cuda.device_count() < 2, reason="test requires multi-GPU machine")
# @pytest.mark.parametrize('cli_args', [dp_16_args])
# def test_examples_dp_image_classifier(cli_args):
#     from pl_examples.basic_examples.image_classifier import cli_main
#
#     with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
#         cli_main()


# TODO
# @pytest.mark.skipif(torch.cuda.device_count() < 2, reason="test requires multi-GPU machine")
# @pytest.mark.parametrize('cli_args', [dp_16_args])
# def test_examples_dp_autoencoder(cli_args):
#     from pl_examples.basic_examples.autoencoder import cli_main
#
#     with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
#         cli_main()


# TODO
# @pytest.mark.skipif(torch.cuda.device_count() < 2, reason="test requires multi-GPU machine")
# @pytest.mark.parametrize('cli_args', [ddp_args])
# def test_examples_ddp_mnist(cli_args):
#     from pl_examples.basic_examples.mnist import cli_main
#
#     with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
#         cli_main()


# TODO
# @pytest.mark.skipif(torch.cuda.device_count() < 2, reason="test requires multi-GPU machine")
# @pytest.mark.parametrize('cli_args', [ddp_args])
# def test_examples_ddp_image_classifier(cli_args):
#     from pl_examples.basic_examples.image_classifier import cli_main
#
#     with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
#         cli_main()


# TODO
# @pytest.mark.skipif(torch.cuda.device_count() < 2, reason="test requires multi-GPU machine")
# @pytest.mark.parametrize('cli_args', [ddp_args])
# def test_examples_ddp_autoencoder(cli_args):
#     from pl_examples.basic_examples.autoencoder import cli_main
#
#     with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
#         cli_main()
#

@pytest.mark.parametrize('cli_args', [cpu_args])
def test_examples_cpu(cli_args):
    from pl_examples.basic_examples.mnist import cli_main as mnist_cli
    from pl_examples.basic_examples.image_classifier import cli_main as ic_cli
    from pl_examples.basic_examples.autoencoder import cli_main as ae_cli

    for cli_cmd in [mnist_cli, ic_cli, ae_cli]:
        with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
            cli_cmd()


@pytest.mark.skipif(not DALI_AVAILABLE, reason="Nvidia DALI required")
@pytest.mark.skipif(not torch.cuda.is_available(), reason="test requires GPU machine")
@pytest.mark.skipif(platform.system() != 'Linux', reason='Only applies to Linux platform.')
@pytest.mark.parametrize('cli_args', [cpu_args])
def test_examples_mnist_dali(cli_args):
    from pl_examples.basic_examples.mnist_dali import cli_main

    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
        cli_main()
