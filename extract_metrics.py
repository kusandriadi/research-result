import os
import re
import csv
from pathlib import Path
from collections import defaultdict

# Base directory
base_dir = r'C:\Users\kusan\Documents\code\research-result\basic\2508'

# Find all log files
log_files = []
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.log'):
            log_files.append(os.path.join(root, file))

print(f'Found {len(log_files)} log files')

# Extract data from each log file
data = []
for log_file in log_files:
    try:
        # Parse path to get model, dataset, scale
        path_parts = Path(log_file).parts
        model = None
        dataset = None
        scale = None
        
        # Find model name from path
        for part in path_parts:
            if 'RealESRGAN' in part and not part.endswith('.log'):
                model = part
                break
        
        # Find dataset and scale
        for i, part in enumerate(path_parts):
            if part in ['BSD100', 'Set14', 'Set5', 'Urban100']:
                dataset = part
                if i + 1 < len(path_parts) and path_parts[i + 1].isdigit():
                    scale = path_parts[i + 1]
                break
        
        if not all([model, dataset, scale]):
            print(f'Skipping {log_file}: missing model={model}, dataset={dataset}, scale={scale}')
            continue
            
        # Read log file content
        with open(log_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metrics using regex
        # Model parameters
        total_params = re.search(r'Total parameters: ([\d,]+)', content)
        model_size = re.search(r'Model size \(calculated\): ([\d.]+) MB', content)
        
        # Image quality metrics
        psnr = re.search(r'PSNR \(HB\): ([\d.]+)', content)
        ssim = re.search(r'SSIM \(HB\): ([\d.]+)', content)
        pi = re.search(r'PI\s+\(LB\): ([\d.]+)', content)
        niqe = re.search(r'NIQE \(LB\): ([\d.]+)', content)
        lpips = re.search(r'LPIPS \(LB\): ([\d.]+)', content)
        
        # Store extracted data
        if all([total_params, model_size, psnr, ssim, pi, niqe, lpips]):
            data.append({
                'model': model,
                'dataset': dataset,
                'scale': scale,
                'psnr': float(psnr.group(1)),
                'ssim': float(ssim.group(1)),
                'pi': float(pi.group(1)),
                'niqe': float(niqe.group(1)),
                'lpips': float(lpips.group(1)),
                'parameters': int(total_params.group(1).replace(',', '')),
                'model_size': float(model_size.group(1))
            })
            print(f'Processed: {model} - {dataset} - scale {scale}')
        else:
            print(f'Missing metrics in {log_file}')
        
    except Exception as e:
        print(f'Error processing {log_file}: {e}')

print(f'\nSuccessfully extracted data from {len(data)} log files')

# Group data by model and dataset
model_dataset_groups = defaultdict(list)
for item in data:
    key = (item['model'], item['dataset'])
    model_dataset_groups[key].append(item)

# Calculate dataset averages (2_dataset_results.csv)
dataset_results = []
for (model, dataset), items in model_dataset_groups.items():
    if items:
        avg_metrics = {
            'Model': model,
            'Dataset': dataset,
            'Avg_PSNR': round(sum(item['psnr'] for item in items) / len(items), 4),
            'Avg_SSIM': round(sum(item['ssim'] for item in items) / len(items), 4),
            'Avg_PI': round(sum(item['pi'] for item in items) / len(items), 4),
            'Avg_NIQE': round(sum(item['niqe'] for item in items) / len(items), 4),
            'Avg_LPIPS': round(sum(item['lpips'] for item in items) / len(items), 4),
            'Parameters': items[0]['parameters'],
            'ModelSize_MB': items[0]['model_size']
        }
        dataset_results.append(avg_metrics)

# Calculate global averages (1_global_result.csv)
model_groups = defaultdict(list)
for item in data:
    model_groups[item['model']].append(item)

global_results = []
for model, items in model_groups.items():
    if items:
        avg_metrics = {
            'Model': model,
            'Avg_PSNR': round(sum(item['psnr'] for item in items) / len(items), 4),
            'Avg_SSIM': round(sum(item['ssim'] for item in items) / len(items), 4),
            'Avg_PI': round(sum(item['pi'] for item in items) / len(items), 4),
            'Avg_NIQE': round(sum(item['niqe'] for item in items) / len(items), 4),
            'Avg_LPIPS': round(sum(item['lpips'] for item in items) / len(items), 4),
            'Parameters': items[0]['parameters'],
            'ModelSize_MB': items[0]['model_size']
        }
        global_results.append(avg_metrics)

# Calculate scale-specific averages (3_dataset-enlargement_results.csv)
scale_groups = defaultdict(list)
for item in data:
    key = (item['model'], item['dataset'], item['scale'])
    scale_groups[key].append(item)

scale_results = []
for (model, dataset, scale), items in scale_groups.items():
    if items:
        for item in items:  # Each scale result is individual
            scale_metrics = {
                'Model': model,
                'Dataset': dataset,
                'Scale': scale,
                'PSNR': item['psnr'],
                'SSIM': item['ssim'],
                'PI': item['pi'],
                'NIQE': item['niqe'],
                'LPIPS': item['lpips'],
                'Parameters': item['parameters'],
                'ModelSize_MB': item['model_size']
            }
            scale_results.append(scale_metrics)

# Write CSV files
output_dir = r'C:\Users\kusan\Documents\code\research-result\basic\2508'

# Write global results
with open(os.path.join(output_dir, '1_global_result.csv'), 'w', newline='', encoding='utf-8') as f:
    if global_results:
        writer = csv.DictWriter(f, fieldnames=global_results[0].keys())
        writer.writeheader()
        writer.writerows(global_results)

# Write dataset results
with open(os.path.join(output_dir, '2_dataset_results.csv'), 'w', newline='', encoding='utf-8') as f:
    if dataset_results:
        writer = csv.DictWriter(f, fieldnames=dataset_results[0].keys())
        writer.writeheader()
        writer.writerows(dataset_results)

# Write scale results
with open(os.path.join(output_dir, '3_dataset-enlargement_results.csv'), 'w', newline='', encoding='utf-8') as f:
    if scale_results:
        writer = csv.DictWriter(f, fieldnames=scale_results[0].keys())
        writer.writeheader()
        writer.writerows(scale_results)

print(f'\nGenerated CSV files:')
print(f'- Global results: {len(global_results)} models')
print(f'- Dataset results: {len(dataset_results)} model-dataset combinations')
print(f'- Scale results: {len(scale_results)} individual results')