  form = LoginForm()
  msg = None

  if request.method == 'POST':
    if form.is_valid():
      print("############### FORM BEGINS ###############")
      print(form.cleaned_data.get("username"))
    else:
      msg = "Error validating form. Please try again"
  
  return render(request, 'accounts/login.html', context={'form': form, 'msg': msg})
