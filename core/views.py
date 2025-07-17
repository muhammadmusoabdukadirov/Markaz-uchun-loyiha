from django.shortcuts import render, get_object_or_404, redirect
from .models import Fan, Ustoz, Aloqa
from django.contrib.auth.decorators import login_required
from .forms import AloqaForm, UstozForm
from datetime import date, timedelta
from django.views.decorators.http import require_POST
from .telegram import send_telegram_message
from django.contrib import messages


def home(request):
    fanlar = Fan.objects.all()
    return render(request, 'core/fanlar.html', {'fanlar': fanlar})


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
    fan = get_object_or_404(Fan, id=fan_id)
    fan.delete()
    return redirect('fanlar_boshqaruv')


@login_required
def fan_ozgartirish(request, fan_id):
    fan = get_object_or_404(Fan, id=fan_id)
    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        if nomi:
            fan.nomi = nomi
            fan.save()
            return redirect('fanlar_boshqaruv')
    return render(request, 'core/fan_ozgartirish.html', {'fan': fan})


@login_required
def ustoz_qoshish(request):
    fanlar = Fan.objects.all()

    if request.method == 'POST':
        form = UstozForm(request.POST, request.FILES)
        if form.is_valid():
            ustoz = form.save()

            # ✅ Telegramga habar yuborish:
            message = f"""
📚 Yangi ustoz qo‘shildi:
👨‍🏫 Ism: {ustoz.ism}
📘 Fan: {ustoz.fan.nomi}
🎓 Daraja: {ustoz.daraja}
🕒 Tajriba: {ustoz.tajriba_yil} yil
            """
            send_telegram_message(message)

            messages.success(request, '✅ Muvaffaqiyatli qo‘shildi va Telegramga yuborildi.')
            return redirect('ustozlar_boshqaruv')
        else:
            messages.error(request, '❌ Formada xatolik bor. Qayta urinib ko‘ring.')
    else:
        form = UstozForm()

    return render(request, 'core/ustoz_qoshish.html', {
        'form': form,
        'fanlar': fanlar
    })


@login_required
def ustozlar_boshqaruv(request):
    fanlar = Fan.objects.all()
    ustozlar = Ustoz.objects.all()
    return render(request, 'core/ustozlar_boshqaruv.html', {
        'ustozlar': ustozlar,
        'fanlar': fanlar
    })


@login_required
def ustoz_ozgartirish(request, ustoz_id):
    ustoz = get_object_or_404(Ustoz, id=ustoz_id)
    fanlar = Fan.objects.all()

    if request.method == 'POST':
        ustoz.ism = request.POST.get('ism')
        ustoz.tajriba_yil = request.POST.get('tajriba_yil')
        ustoz.daraja = request.POST.get('daraja')
        ustoz.tavsif = request.POST.get('tavsif')
        fan_id = request.POST.get('fan')
        if fan_id:
            ustoz.fan = Fan.objects.get(id=fan_id)
        if request.FILES.get('rasm'):
            ustoz.rasm = request.FILES.get('rasm')
        ustoz.save()
        return redirect('ustozlar_boshqaruv')

    return render(request, 'core/ustoz_ozgartirish.html', {'ustoz': ustoz, 'fanlar': fanlar})


@login_required
def ustoz_ochirish(request, ustoz_id):
    ustoz = get_object_or_404(Ustoz, id=ustoz_id)
    ustoz.delete()
    return redirect('ustozlar_boshqaruv')


@login_required
def aloqalar(request):
    today = date.today()
    yesterday = today - timedelta(days=1)

    aloqalar = Aloqa.objects.select_related('ustoz__fan').order_by('-sana')

    bugun, kecha, qolgan = [], [], []
    for aloqa in aloqalar:
        aloqa_sana = aloqa.sana.date()
        if aloqa_sana == today:
            bugun.append(aloqa)
        elif aloqa_sana == yesterday:
            kecha.append(aloqa)
        else:
            qolgan.append(aloqa)

    return render(request, 'core/aloqalar.html', {
        'bugun': bugun,
        'kecha': kecha,
        'qolgan': qolgan
    })


@require_POST
@login_required
def aloqa_ochirish(request, aloqa_id):
    aloqa = get_object_or_404(Aloqa, id=aloqa_id)
    aloqa.delete()
    return redirect('aloqalar')


@login_required
def ustozlar(request, fan_id):
    fan = get_object_or_404(Fan, id=fan_id)
    ustozlar = Ustoz.objects.filter(fan=fan)

    return render(request, 'core/ustozlar.html', {
        'fan': fan,
        'ustozlar': ustozlar
    })
