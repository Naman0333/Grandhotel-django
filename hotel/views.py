from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .forms import ContactForm, BookingForm
from django.contrib import messages
from .models import Contact,Room,Facility, Dining, Booking
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError

    
def hotel(request):
    return render(request,'home.html')

def rooms(request):
    rooms = Room.objects.filter(available = True)
    context = {'rooms' : rooms}
    return render(request, 'rooms.html',context)

def booking(request,room_id):
    room_type = get_object_or_404(Room, id = room_id)
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid(): 
            email  = form.cleaned_data['email']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            try: 
                validate_booking_date(email,check_in,check_out)
                booking = form.save(commit=False)
                booking.room_type = room_type
                booking.save()
                #send order recieved email to customer
                mail_subject = 'Order Confirmation'
                message = render_to_string('booking_confirmation.html')
                to_email = email
                send_email = EmailMessage(mail_subject, message, to=[to_email])
                send_email.send()
                messages.success(request, 'Your booking request was sent successfully. Thank you for contacting us!')
                return redirect('booking',room_id)
            except ValueError as e:
                messages.error(request,str(e))
                return redirect('booking',room_id)
                
            
    else:
        form = BookingForm()

    context = {
        'form': form,
        'room_type': room_type,
    }
    return render(request, 'booking.html', context)


def validate_booking_date(email, check_in, check_out):
    bookings = Booking.objects.filter(email=email, check_in=check_in, check_out=check_out)
    if bookings.exists():
        msg = f"Sorry, the room is already booked for the selected dates by {email}. Please select different dates or choose different room"
        raise ValueError(msg)
    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save() 
            #send order recieved email to customer
            mail_subject = 'Thank you for your order!'
            message = render_to_string('contact_success.html')
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Your message was sent successfully. Thank you for contacting us!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html',{'from' : form})


def about(request):
    return render(request, 'about.html')

def facilities(request):
    facilities = Facility.objects.all()
    return render(request, 'facilities.html',{'facilities': facilities})


def dining(request):
    dining_data = Dining.objects.all()
    context = {
        'dining_data': dining_data
    }
    return render(request, 'dining.html', context)
    



def newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # Do something with the email value, such as send a confirmation email
        mail_subject = 'Thank you for subscribing!'
        message = render_to_string('thankyou.html')
        to_email = email
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()
        return render(request,'newsletter_subscribe_thankyou.html')
    else:
        return render(request,'home.html')



