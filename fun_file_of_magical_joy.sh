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
python ~/CIS_732/least_squares_GAN.py
 

 

torchrun --standalone --nnodes=1 --nproc_per_node=2 \

/homes/benv86/Projects/CIS830/pfgmpp/train.py \

--outdir=training-runs --data=/homes/benv86/Projects/CIS830/64BadBale.zip --cond=0 --batch=64 --pfgmpp=1 --duration=50 --resolution=64
