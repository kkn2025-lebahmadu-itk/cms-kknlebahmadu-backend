
# SETUP

Buat virtual environment (kalau belum ada)
```
python -m venv venv
```

setelah itu, aktifkan virtual environment
### bash
```
source venv/scripts/activate
```
atau
### powershell
```
./venv/Scripts/activate
```
atau
```
./venv/Scripts/activate.ps1
```

# LIBRARY DEPENDENCIES

### Install
Setelah mengaktifkan virtual environment, install semua dependencies 
```
pip install -r requirements.txt
```

### Tambah dependency
jika ada library baru yang perlu ditambahkan,
```
pip freeze > requirements.txt
```
atau tambah secara manual di `./requirements.txt`

# WORKFLOW

### 1. Fetch dari remote repo
```
git fetch
```
selalu git fetch jika akan mengerjakan

### 2. Code
dan saya mohon tulis kode yang bersih :(     
biar scalable

### 3. (OPTIONAL) Branching
buat branch kalo mau ngerjain fitur baru, dan rebase

### 4. Commit & Push
jangan lupa tulis commmit message yang bagus


#### NOTE :
Kalau buat script (.bat , .sh , dkk), jangan lupa masukin ke `.gitignore`
# RUN

buat superuser dulu kalau belum ada (buat akses /admin-panel), run
```
python manage.py createsuperuser
```


dari root directory, run 
```
python manage.py runserver
```