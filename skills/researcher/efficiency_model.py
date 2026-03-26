import numpy as np

def project_zero_efficiency(query_vector, data_manifold, time_delta):
    """
    Calculates the 4D efficiency of a research trajectory.
    
    Dimensions:
    x, y, z : Semantic Space (Context, Domain, Sentiment)
    w       : Temporal Dimension (Velocity of Information)
    
    The 4th dimension (time) is what humans experience that AI tends to miss.
    AI thinks linearly; humans experience time as a dimension.
    """
    
    # 1. Semantic Distance (The 3D 'Where')
    # Measures how far the 'Puppet' must travel in latent space to find the data
    dist = np.linalg.norm(query_vector[:3] - data_manifold[:3])
    
    # 2. Temporal Flux (The 4th Dimension 'When')
    # High flux means the info is changing fast (volatile); low flux is 'stable ground truth'
    flux = np.abs(data_manifold[3] * time_delta)
    
    # 3. Orchestration Tension (The 'Strings')
    # The Puppet Master's ability to constrain the search to a specific path
    # Higher tension = narrower, more efficient focus (less 'drift')
    tension = 1 / (1 + dist)
    
    # 4. The 4D Efficiency Score (E)
    # Efficiency is maximized when Distance is low and Tension is high, 
    # modulated by the stability (Flux) of the information over time.
    efficiency = (tension * np.exp(-flux)) / (1 + dist**2)
    
    return round(efficiency, 4)


# Example: Researching a fast-moving AI trend
if __name__ == "__main__":
    target_idea = np.array([0.9, 0.2, 0.5, 0.8])  # [x, y, z, temporal_velocity]
    current_state = np.array([0.85, 0.15, 0.45, 0.75])
    time_lookahead = 1.0  # Looking 1 unit into the future
    
    score = project_zero_efficiency(target_idea, current_state, time_lookahead)
    print(f"4D Trajectory Efficiency: {score}")
