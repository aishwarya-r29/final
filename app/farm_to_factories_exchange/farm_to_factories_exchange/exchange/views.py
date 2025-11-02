from django.shortcuts import render

FARMER_BATCHES = [
    {
        'id': 1,
        'farmer_name': 'Green Valley Farm',
        'product': 'Organic Tomatoes',
        'quantity': '500 kg',
        'harvest_date': '2025-10-15',
        'price': '$2.50/kg'
    },
    {
        'id': 2,
        'farmer_name': 'Sunrise Orchards',
        'product': 'Fresh Apples',
        'quantity': '1000 kg',
        'harvest_date': '2025-10-20',
        'price': '$1.80/kg'
    },
    {
        'id': 3,
        'farmer_name': 'Golden Fields Co-op',
        'product': 'Wheat Grain',
        'quantity': '2000 kg',
        'harvest_date': '2025-10-10',
        'price': '$0.50/kg'
    },
]

FACTORY_DEMANDS = [
    {
        'id': 1,
        'factory_name': 'Fresh Foods Processing',
        'product_needed': 'Tomatoes',
        'quantity': '600 kg',
        'budget': '$1500',
        'deadline': '2025-11-15'
    },
    {
        'id': 2,
        'factory_name': 'Apple Juice Corp',
        'product_needed': 'Apples',
        'quantity': '800 kg',
        'budget': '$1440',
        'deadline': '2025-11-20'
    },
    {
        'id': 3,
        'factory_name': 'Global Grain Mills',
        'product_needed': 'Wheat',
        'quantity': '1500 kg',
        'budget': '$750',
        'deadline': '2025-11-10'
    },
]

MATCHES = [
    {
        'farmer': 'Green Valley Farm',
        'product': 'Organic Tomatoes',
        'factory': 'Fresh Foods Processing',
        'match_score': 92,
        'explanation': 'High-quality organic tomatoes match factory demand. Price within budget and harvest date meets deadline.',
        'farmer_quantity': '500 kg',
        'factory_quantity': '600 kg',
        'compatibility': 'Excellent'
    },
    {
        'farmer': 'Sunrise Orchards',
        'product': 'Fresh Apples',
        'factory': 'Apple Juice Corp',
        'match_score': 88,
        'explanation': 'Fresh apples available in required quantity. Competitive pricing and meets quality standards.',
        'farmer_quantity': '1000 kg',
        'factory_quantity': '800 kg',
        'compatibility': 'Very Good'
    },
    {
        'farmer': 'Golden Fields Co-op',
        'product': 'Wheat Grain',
        'factory': 'Global Grain Mills',
        'match_score': 85,
        'explanation': 'Premium wheat grain meets factory specifications. Sufficient quantity and favorable delivery timeline.',
        'farmer_quantity': '2000 kg',
        'factory_quantity': '1500 kg',
        'compatibility': 'Good'
    },
]

def landing(request):
    return render(request, 'exchange/landing.html')

def farmer_dashboard(request):
    context = {
        'batches': FARMER_BATCHES
    }
    return render(request, 'exchange/farmer_dashboard.html', context)

def factory_dashboard(request):
    context = {
        'demands': FACTORY_DEMANDS
    }
    return render(request, 'exchange/factory_dashboard.html', context)

def upload_batch(request):
    return render(request, 'exchange/upload_batch.html')

def post_demand(request):
    return render(request, 'exchange/post_demand.html')

def matches(request):
    context = {
        'matches': MATCHES
    }
    return render(request, 'exchange/matches.html', context)
