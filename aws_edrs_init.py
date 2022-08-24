def init_edr_service():
    """
    Initialize the DR Service for an account for first time
    """    
    client = session.client('drs')
    init_response = client.initialize_service()
    logger.info(init_response)