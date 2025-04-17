import pandas as pd
import os
import glob

def combine_csv_files_efficiently(folder_path, output_file, chunk_size=10000):
    all_files = glob.glob(os.path.join(folder_path, "*.csv"))

    # Open output file in write mode initially, then append
    first_file = True
    for file in all_files:
        # Read file in chunks
        chunk_iter = pd.read_csv(file, chunksize=chunk_size)

        for chunk in chunk_iter:
            if first_file:
                chunk.to_csv(output_file, mode='w', index=False)
                first_file = False
            else:
                chunk.to_csv(output_file, mode='a', index=False, header=False)

# Usage
combine_csv_files_efficiently(
    folder_path="E:/UOM/My-CODE_RUSH/projects/SL-MOBILITY/Data/d51d20c2-3c75-4c51-b344-722a01fb5f48/msg",
    output_file="combined_data5.csv",
    chunk_size=10000  # You can adjust based on your available RAM
)
