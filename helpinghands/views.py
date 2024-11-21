from datetime import date
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout
from .models import *
from .forms import PaymentForm
import razorpay
# Create your views here.
def index(request):
    return render(request,'index.html')

def all_logins(request):
    return render(request,'all_logins.html')

def donor_login(request):
    if request.method == "POST":
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            auth_login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request,'donor_login.html',locals())

def admin_login(request):
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                auth_login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'admin_login.html',locals())

def organization_login(request):
    return render(request,'organization_login.html')

def donor_reg(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        address = request.POST['address']
        userpic = request.FILES['userpic']

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            Donor.objects.create(user=user, contact=contact, address=address, userpic=userpic)
            error = "no"
        except Exception as e:
            error = "yes"
            print(e)
    return render(request,'donor_reg.html',locals())

def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request, 'donor_home.html',locals())

def donate_now(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    if request.method == "POST":
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        collectionloc = request.POST['collectionloc']
        description = request.POST['description']
        try:
            Donation.objects.create(donor=donor,donationname=donationname,donationpic=donationpic,collectionloc=collectionloc,description=description,status="pending")
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    return render(request, 'donate_now.html',locals())

def donor_base(request):
    return render(request,'donor_base.html',locals())

def donation_history(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    return render(request, 'donation_history.html', locals())
def Logout(request):
    logout(request)
    return redirect('index')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html',locals())

def pending_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.filter(status="pending")
    return render(request, 'pending_donation.html', locals())

def view_donationdetails(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']
        try:
            donation.adminremark = adminremark
            donation.status = status
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'view_donationdetails.html', locals())

def accepted_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.filter(status="accept")
    return render(request, 'accepted_donation.html', locals())

def add_area(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        areaname = request.POST['areaname']
        address = request.POST['address']
        description = request.POST['description']
        try:
            Organization.objects.create(areaname=areaname, description=description,address=address)
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    return render(request, 'add_area.html',locals())

def manage_area(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    area = Organization.objects.all()
    return render(request, 'manage_area.html', locals())

def edit_area(request, pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('admin_login')
    area = Organization.objects.get(id=pid)
    if request.method == "POST":
        areaname = request.POST['areaname']
        address = request.POST['address']
        description = request.POST['description']
        area.areaname=areaname
        area.address = address
        area.description=description
        try:
            area.save()
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    return render(request, 'edit_area.html',locals())

def delete_area(request,pid):
    area = Organization.objects.get(id=pid)
    area.delete()
    return redirect('manage_area')

def manage_donor(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.all()
    return render(request, 'manage_donor.html', locals())

def view_donordetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.get(id=pid)
    return render(request, 'view_donordetail.html',locals())

def delete_donor(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('manage_donor')

def volunteer_reg(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        idpic = request.FILES['idpic']
        address = request.POST['address']
        aboutme = request.POST['aboutme']

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            Volunteer.objects.create(user=user, contact=contact, userpic=userpic, idpic=idpic, address=address,
                                     aboutme=aboutme, status="pending")
            error = "no"
        except Exception as e:
            error = "not"
            print(e)
    return render(request, 'volunteer_reg.html', locals())

def volunteer_login(request):
    if request.method == "POST":
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Volunteer.objects.get(user=user)
                if user1.status != "pending":
                    auth_login(request, user)
                    error = "no"
                else:
                    error = "not"

            except:
                error = "yes"
        else:
            error = "yes"
    return render(request,'volunteer_login.html',locals())

def volunteer_home(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    return render(request, 'volunteer_home.html',locals())

def new_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.all()
    return render(request, 'new_volunteer.html', locals())

def view_volunteerdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']
        try:
            volunteer.adminremark = adminremark
            volunteer.status = status
            volunteer.updationdate = date.today()
            volunteer.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'view_volunteerdetail.html', locals())

def accepted_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(status="accept")
    return render(request, 'accepted_volunteer.html', locals())
def rejected_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(status="reject")
    return render(request, 'rejected_volunteer.html', locals())

def all_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.all()
    return render(request, 'all_volunteer.html', locals())

def delete_volunteer(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('all_volunteer')

def accepted_donationdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id=pid)
    donationarea = Organization.objects.all()
    volunteer = Volunteer.objects.all()
    donor = Donor.objects.all()
    if request.method == "POST":
        donationareaid = request.POST['donationareaid']
        volunteerid = request.POST['volunteerid']

        da = Organization.objects.get(id=donationareaid)
        v = Volunteer.objects.get(id=volunteerid)

        try:
            donation.donationarea = da
            donation.volunteer = v

            donation.status = 'Volunteer Allocated'
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'accepted_donationdetail.html', locals())

def collection_request(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer,status="Volunteer Allocated")
    return render(request, 'collection_request.html', locals())

def donation_collectiondetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        volunteerremark = request.POST['volunteerremark']

        try:
            donation.status = status
            donation.volunteerremark = volunteerremark
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except Exception as e:
            error = "yes"
    return render(request, 'donation_collectiondetail.html', locals())

def donationreceived_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer,status="Donation Received")
    return render(request, 'donationreceived_volunteer.html', locals())

def donationreceived_detail(request, pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        deliverypic = request.FILES['deliverypic']

        try:
            donation.status = status
            donation.updationdate = date.today()
            donation.save()
            Gallery.objects.create(donation=donation,deliverypic=deliverypic)
            error = "no"
        except Exception as e:
            error = "yes"
    return render(request, 'donationreceived_detail.html', locals())

def donationnotreceived_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer,status="Donation Not Received")
    return render(request, 'donationnotreceived_volunteer.html', locals())

def donationDelivered_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer,status="Donation Delivered successfully")
    return render(request, 'donationDelivered_volunteer.html', locals())

def profile_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    error = ""
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        idpic = request.FILES['idpic']
        address = request.POST['address']
        aboutme = request.POST['aboutme']

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            Volunteer.objects.create(user=user, contact=contact, userpic=userpic, idpic=idpic, address=address,
                                     aboutme=aboutme, status="pending")
            error = "no"
        except Exception as e:
            error = "not"
            print(e)
    return render(request, 'profile_volunteer.html', locals())


def indexforpayment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        # creating a razorpay client
        client = razorpay.Client(auth=('rzp_test_eNnWDVb2Sd8t8l', 'hf9DL54rKotJ2BFou9PFNrfC'))
    #     creating a order
        response_payment = client.order.create(dict(amount=amount,
                                                    currency= 'INR')
                                               )
        print(response_payment)
        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            paymentdetails = PaymentDetails(
                name = name,
                amount = amount,
                order_id = order_id
            )
            paymentdetails.save()
            response_payment['name'] = name
            form = PaymentForm(request.POST or None)
            return render(request, "indexforpayment.html", {'form': form, 'payment': response_payment})

    form = PaymentForm()
    return render(request, "indexforpayment.html", {'form': form})

def successforpayment(request):

    response = request.POST
    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }

    client = razorpay.Client(auth=('rzp_test_eNnWDVb2Sd8t8l', 'hf9DL54rKotJ2BFou9PFNrfC'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        paymentdetails = PaymentDetails.objects.get(order_id=response['razorpay_order_id'])
        paymentdetails.razorpay_payment_id = response['razorpay_payment_id']
        paymentdetails.paid = True
        paymentdetails.save()
        return render(request, 'successforpayment.html', {'status': True})
    except:
        return render(request, 'successforpayment.html', {'status': False})



def baseforpayment(request):
    return render(request,'baseforpayment.html')
