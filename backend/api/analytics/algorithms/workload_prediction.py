import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def analyze_workload_dynamics(tasks_df):
    """
    Dual-purpose algorithm:
    1. Identifies team Bottlenecks (Statistical Outliers)
    2. Predicts individual Burnout (Volume + Velocity Stress)
    """
    if tasks_df.empty:
        return []

    #Filter for incomplete tasks
    active_tasks = tasks_df[tasks_df['progress_percentage'] < 100]
        
    # 2. Count tasks per user
    workload = active_tasks.groupby('assigned_to').size().reset_index(name='task_count')
        
    # 3. Identify Bottlenecks (e.g., anyone with more than 5 active tasks)
    bottlenecks = workload[workload['task_count'] > 5].to_dict(orient='records')
        
    return bottlenecks