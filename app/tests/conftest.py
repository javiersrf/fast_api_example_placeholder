import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

@pytest.fixture
def auth_header():
    return {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdGUiLCJleHBpcmVkX2RhdGUiOiJ5eXl5LU1NLWRkIEhIOm1tOnNzLlNTUyBaIn0.IjptA6-THcjLWCs1x6kkXN-o0U0CnXU4IZc44NrK3FY"
    }