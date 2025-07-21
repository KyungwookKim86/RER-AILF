import numpy as np

φ = 1.618033988749
α, β, γ, δ = (φ**3, φ**2, φ, 1)
α, β, γ, δ = np.array([α, β, γ, δ]) / sum([α, β, γ, δ])

def p_ree(R, S, T, G, η=0.0):
    x = α * R + β * S + γ * T + δ * G + η
    return 1.0 / (1.0 + np.exp(-np.clip(x, -500, 500)))  # 로지스틱 시그모이드