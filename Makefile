all: venv test_behave unittests

venv:
    python -m venv venv3
    #for windows
    venv3\Scripts\activate
    #for macOS or linux, use the below command
    #source venv3/bin/activate
    pip install -r requirements.txt


test_behave:
    behave -f allure_behave.formatter:AllureFormatter -o reports
    #for windows need to run it from powershell
    #allure serve reports

unittests:
    pytest -v unit_tests/test_calculator_modal.py --html=pytest_report.html --self-contained-html

clean:
    rm -rf pytest_report.html
    rm -rf reports/*
