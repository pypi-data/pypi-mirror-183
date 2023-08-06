"""HOMEPAGE_ID_CLASSIFICATION_MODEL_PARAMETER"""
HOMEPAGE_ID_CLF_MODEL = {
    "epochs": 100,
    "n_splits": 5,
    "n_repeats": 3,
    "random_state": 1,
    "verbose": 1,
    "current_model_name": "homepage_id_clf_model_v1.pkl",
}

HOMEPAGE_IDS_CONTENT_REC_MODEL = {
    "cv": 10,
    "measures": ["rmse"],
    "rating_scale": (0, 10),
    "current_model_name": "homepage_ids_content_recommendation_model.pkl",
}

GRID_SEARCH_PARAMETERS = {
    "n_epochs": [50, 100, 150],
    "lr_all": [0.001, 0.002, 0.005],
    "reg_all": [0.02, 0.08, 0.4],
}

HOMEPAGE_ID_VIEW_COUNT_THRESHOLD = 100
NUMBER_OF_DUPLICATE_VIEWS_THRESHOLD = 12

BIASED_HOMEPAGE_IDS = [306, 669]
BIASED_CUSTOMER_ID = 0

MIN_CONTENT_HAVING_RATING = 5
MIN_USER_GIVEN_RATING = 5
