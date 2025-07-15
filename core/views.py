from django.shortcuts import render, get_object_or_404, redirect, redirect
from .models import Fan, Ustoz, Aloqa
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    fanlar = Fan.objects.all()
    return render(request, 'core/fanlar.html', {'fanlar': fanlar})

def ustozlar(request, fan_id):
    fan = get_object_or_404(Fan, id=fan_id)
    ustozlar = Ustoz.objects.filter(fan=fan).order_by('-daraja')

    if request.method == "POST":
        tel = request.POST.get('tel')
        ustoz_id = request.POST.get('ustoz_id')

        if tel and ustoz_id:
            Aloqa.objects.create(telefon=tel, ustoz_id=ustoz_id)
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi! Tez orada aloqaga chiqamiz.")
        else:
            messages.warning(request, "Iltimos, telefon raqamingizni to‘liq kiriting!")

        return redirect(request.path_info)

    return render(request, 'core/ustozlar.html', {'fan': fan, 'ustozlar': ustozlar})


@login_required
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@login_required
def fanlar_boshqaruv(request):
    fanlar = Fan.objects.all()

    if request.method == "POST":
        nomi = request.POST.get("nomi")
        if nomi:
            Fan.objects.create(nomi=nomi)
            return redirect('fanlar_boshqaruv')

    return render(request, 'core/fanlar_boshqaruv.html', {'fanlar': fanlar})

@login_required
def fan_ochirish(request, fan_id):
    fan = Fan.objects.get(id=fan_id)
    fan.delete()
    return redirect('fanlar_boshqaruv')


@login_required
def ustozlar_boshqaruv(request):
    fanlar = Fan.objects.all()
    ustozlar = Ustoz.objects.all()

    if request.method == 'POST':
        ism = request.POST.get('ism')
        tajriba = request.POST.get('tajriba_yil')
        daraja = request.POST.get('daraja')
        fan_id = request.POST.get('fan')
        tavsif = request.POST.get('tavsif')

        if ism and tajriba and daraja and fan_id and tavsif:
            fan = Fan.objects.get(id=fan_id)
            Ustoz.objects.create(
                ism=ism,
                tajriba_yil=tajriba,
                daraja=daraja,
                fan=fan,
                tavsif=tavsif
            )
            return redirect('ustozlar_boshqaruv')

    return render(request, 'core/ustozlar_boshqaruv.html', {'ustozlar': ustozlar, 'fanlar': fanlar})

@login_required
def ustoz_ochirish(request, ustoz_id):
    ustoz = get_object_or_404(Ustoz, id=ustoz_id)
    ustoz.delete()
    return redirect('ustozlar_boshqaruv')
