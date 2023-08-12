#!/bin/bash
#SBATCH --gpus-per-node=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:30:00
#SBATCH --mem=15GB

module purge

source /scratch/s5382726/toucan/bin/activate

python3 run_training_pipeline.py fine_abkhaz --gpu_id "0"
