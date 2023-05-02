#!/bin/bash
#SBATCH --mem-per-cpu=200G
#SBATCH --time=5-23:15:02
#SBATCH --partition=ksu-gen-gpu.q
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --output=output.o%j
#SBATCH -J output
#SBATCH --mail-type=END
#SBATCH --mail-user bweinhold@ksu.edu

module load Python/3.9.6-GCCcore-11.2.0
source ~/virtual_envs/GAN/bin/activate
export PYTHONDONTWRITEBYTeECODE=1
python /homes/bweinhold/CIS_732/ultralytics/ytest_loader.py


