get_response_avl_num = {
    "type": "object",
    "patternProperties": {
        "^[a-z]{2,3}_\\d$": {
            "type": "string",
            "pattern": "^[0-9]+$"
        }
    },
    "additionalProperties": False
}
