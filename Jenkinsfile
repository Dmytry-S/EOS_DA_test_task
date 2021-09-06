node {
    stage("Checkout Repo"){
        git branch: 'main',
        url: 'https://github.com/Dmytry-S/EOS_DA_test_task.git'
    }

    stage("Create venv & run test"){
        sh 'virtualenv venv && pip install -r requirements.txt && pytest test_login_page.py'
    }
}