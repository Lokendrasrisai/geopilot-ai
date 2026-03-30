def inject_css():
    return '''
    <style>
    .block-container {padding-top: 1.4rem; padding-bottom: 2rem; max-width: 1280px;}
    .hero {
        padding: 1.4rem 1.5rem;
        border-radius: 26px;
        background: linear-gradient(135deg, rgba(2,6,23,0.98), rgba(15,23,42,0.86));
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 28px 60px rgba(2,6,23,0.32);
        margin-bottom: 1rem;
    }
    .hero h1 {font-size: 2.3rem; margin: 0 0 0.35rem 0; color: white;}
    .hero p {color: #cbd5e1; line-height: 1.75; margin: 0;}
    .glass {
        border-radius: 22px;
        padding: 1rem 1rem;
        background: rgba(15,23,42,0.74);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 0.9rem;
    }
    .section-title {
        color: white;
        font-weight: 700;
        font-size: 1.08rem;
        margin-bottom: 0.45rem;
    }
    .score-pill {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: rgba(56,189,248,0.16);
        color: #bae6fd;
        font-weight: 700;
        margin-bottom: 0.7rem;
    }
    div[data-testid="stMetricValue"] {font-size: 2rem;}
    </style>
    '''
