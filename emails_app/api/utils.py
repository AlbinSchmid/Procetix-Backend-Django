def extract_optional_fiels(request):
    data = {}
    if request.data.get('processOptimization') == True:
        data["processOptimization"] = True
    if request.data.get('digitalization') == True:
        data["digitalization"] = True
    if request.data.get('websiteDevelopment') == True:
        data["websiteDevelopment"] = True
    if request.data.get('websiteOptimization') == True:
        data["websiteOptimization"] = True
    if request.data.get('consulting') == True:
        data["consulting"] = True

    referral = request.data.get('referral')
    if referral and len(referral) > 0:
        data["referral"] = request.data.get('referral')

    companySize = request.data.get('companySize')
    if companySize and len(companySize) > 0:
            data["companySize"] = request.data.get('companySize')
            
    budget = request.data.get('budget')
    if budget and len(budget) > 0:
            data["budget"] = request.data.get('budget')

    return data