# Code Citations

## License: Unknown
Source: [NLP-LAB](https://github.com/boup/NLP-LAB/tree/d4609128458aff516d43539a51c4023d36b35b01/l21.py)

```regex
^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$  # Regex for phone number validation
```

---

## License: Unknown
Source: [GoGei Blog](https://github.com/GoGei/blog/tree/5ae1bf32859c70aef816deacc4efc15322bae486/core/Utils/validators.py)

```regex
[+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$  # Regex for phone number validation
```

---

## License: MIT
Source: [Flask-Portfolio](https://github.com/dmdhrumilmistry/Flask-Portfolio/tree/526d16adbf6bd9fe738bf858fd910c3b1a923908/app.py)

```python
if request.method == 'POST':
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
```

---

## License: MIT
Source: [Personal-Website](https://github.com/GeorgeVJose/Personal-Website/tree/d7e41b5658875fe0f8780e9b4a3b3e52a9b8137f/app.py)

```python
if 10 <= len(phone) <= 13 and re.fullmatch(r'^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$'):
    # Phone number validation logic
```

---

## License: Unknown
Source: [Portfolio_Python_Flask](https://github.com/Mohamed-Azab07/Portfolio_Python_Flask/tree/e08e4fea77e984aeb0cbebe670d7f33a667f26b6/app.py)

```python
name = request.form.get('name', '').strip()
email = request.form.get('email', '').strip()
phone = request.form.get('phone', '').strip()
reason = request.form.get('reason', '').strip()
```

