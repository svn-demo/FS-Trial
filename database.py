# -*- coding: utf8 -*-
verfying upstream remote configuration
adding trial code
verfiy upstream2
nothing
from ngds.core import model as dbmodel
from ngds.core.model import get_conn

DUMMY_TRIMS = [u"XL", u"STX", u"XLT", u"FX2", u"Lariat", u"FX4", u"Raptor", u"King Ranch", u"Platinum", u"Harley Davidson"]

conn = get_conn()

def url(text, link):
    """ Create a URL in the data model """
    url = dict()
    url['url'] = link
    url['text'] = text
    return url

P_TEXT = u"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
P_AR_TEXT = u'هو بال الثالث الياباني اقتصادية, لم مليون الثالث، يكن, دون أن أواخر الفترة. كرسي أصقاع ومدني، حين بـ, وزارة القادة معاملة فعل هو. من ذلك وقبل بزمام, تعد و بغزو أمدها, ما يكن ٠٨٠٤ فمرّ. قد هذا بداية هاربر الأثنان. وبغطاء واندونيسيا، من يتم, العالم، الإيطالية لمّ أي, ذلك بأيدي الجنرال اقتصادية و. وقبل الحرب، والنفيس تم مكن, بخطوط اقتصّت الضغوط لان قد.'


def sample_site(owner):
    site = conn.DealerSite()
    site['_id'] = u'site%s' % owner
    site['owner'] = owner
    site['theme'] = u'default'
    site['navigation'] = [url(u'Home', u'/'),
                           #url(u'Inventory', u'/inventory/'),
                           #url(u'Preowned', u'/preowned/'),
                           url(u'About Us', u'/about/'),
                           #url(u'Request a Quote', u'/quote/'),
                           url(u'Showroom', u'/showroom/'),
                           #url(u'Contact Us', u'/contact/')
                           url(u'Trade In', u'/tradein/'),
                           url(u'Staff',u'/staff/')
                           ]

    site['dealer_site_data'] = {"dealer_text": P_TEXT,
                                  "hero_shots": [u"img/heroshots/lm.gif"],
                                  "inventory_defaults": {u"Ford": u"Fusion", u"Lincoln": u"MKX"},
                                  'campaigns': [u"img/quads/xkr.jpg", u"img/quads/schedule-test-drive.jpg", u"img/quads/build-your-jaguar.jpg"],
                                  "disclaimers": [P_TEXT, P_TEXT],
                                  "display_phone": u"111-111-1111",
                                  "display_email": u"testcovert@dealerconnection.com",
                                }

    return site


 
def sample_dealerInfo():
    dealer_info = conn.DealerInfo()
    dealer_info['dealer'] = u"04437"

    emp = []
    emp.append(dict(name=u'Sample Empl1',email=u'Sample1@W.com',phone=u'122-123-1234',title=u'Title1',description=u'Description',fax=u'fax'))
    emp.append(dict(name=u'Sample Empl2',email=u'Sample2@W.com',phone=u'122-123-1234',title=u'Title2',description=u'Description2',fax=u'fax'))
    emp.append(dict(name=u'Samba',email=u'Samba2@gmail.com',phone=u'122-123-1234',title=u'Senior Manager',description=u'Senior Level',fax=u'022-21630175'))
    dealer_info['employees'] = emp
    dealer_info.save()
   
    

def sample_dealer(name, code, brands, subdomain):
    dealer = conn.Dealer()
    dealer['_id'] = u'dealer%s' % code
    dealer['name'] = name
    dealer['code'] = code
    dealer['languages'] = ['en','fr','es']
    dealer['brands'] = brands
    dealer['subdomain'] = subdomain
    dealer['country'] = u'US'
    dealer['primaryAddress'] = dict(address=u'123 main street', city=u'Austin', state=u'TX', zip=u'78735')
    dealer['phone'] = u'122-123-1234'

    return dealer


def page(name, path, owner, pagetype, layout=u'default'):
    page = conn.Page()
    page['name'] = name
    page['path'] = path
    page['owner'] = owner
    page['layout'] = layout
    page['type'] = pagetype
    page['_id'] = '_'.join([owner, path])
    return page


def model(name, year, brand, vehicle_type=dbmodel.CARS, trims=DUMMY_TRIMS):
    model_info = conn.ModelInfo()
    model_info["name"] = name
    model_info["year"] = year
    #model_info["vehicle_type"] = vehicle_type
    model_info["trims"] = trims
    model_info["brand"] = brand
    return model_info

if __name__ == '__main__':
    from ngds.core.model import ModelInfo, Dealer, Page, DealerSite

    conn.ngds.drop_collection(Page.__collection__)
    conn.ngds.drop_collection(DealerSite.__collection__)
    conn.ngds.drop_collection(Dealer.__collection__)
    conn.ngds.drop_collection(ModelInfo.__collection__)

    sample_dealer(name=u"Test Covert", code=u"04437", brands=[dbmodel.FORD, dbmodel.LINCOLN], subdomain=u"localhost").save()
    sample_site(owner=u"04437").save()
    page(u"Home Page", u"/", u"04437", u"home").save()
    page(u"Home Page", u"/inventory/", u"04437", u"inventory").save()
    page(u"Request a Quote", u"/quote/", u"04437", u"quote").save()
    page(u"Thank You", u"/thankyou/", u"04437", u"thankyou").save()
    page(u"GES Wizard", u"/ges/", u"04437", u"ges").save()
    page(u"About Us", u"/about/", u"04437", u"about").save()
    page(u"Preowned", u"/preowned/", u"04437", u"preowned").save()
    page(u"Showroom", u"/showroom/", u"04437", u"showroom").save()
    page(u"Contact Us", u"/contact/", u"04437", u"contact").save()
    page(u"Trade In", u"/tradein/", u"04437", u"tradein").save()
    page(u"Staff", u"/staff/", u"04437", u"staff").save()
    # To use this dealer add the following to your hosts file:
    # 
    # 127.0.0.1    fantasticphils.dealerconnection.com

    sample_dealer(name=u"Fantastic Phil's Auto Hut", code=u"04242", brands=[dbmodel.FORD, dbmodel.LINCOLN], subdomain=u"fantasticphils.dealerconnection.com").save()
    sample_site(owner=u"04242").save()
    sample_dealerInfo()
    page(u"Home Page", u"/", u"04242", u"home").save()
    page(u"Home Page", u"/inventory/", u"04242", u"inventory").save()
    page(u"Request a Quote", u"/quote/", u"04242", u"quote").save()
    page(u"Thank You", u"/thankyou/", u"04242", u"thankyou").save()
    page(u"GES Wizard", u"/ges/", u"04242", u"ges").save()
    page(u"About Us", u"/about/", u"04242", u"about").save()
    page(u"Preowned", u"/preowned/", u"04242", u"preowned").save()
    page(u"Showroom", u"/showroom/", u"04242", u"showroom").save()
    page(u"Contact Us", u"/contact/", u"04242", u"contact").save()
    page(u"Trade In", u"/tradein/", u"04242", u"tradein").save()
    page(u"Staff", u"/staff/", u"04242", u"staff").save()

    model(u"Edge", 2012, dbmodel.FORD).save()
    model(u"Taurus", 2012, dbmodel.FORD).save()
    model(u"Fusion", 2012, dbmodel.FORD).save()
    model(u"Focus", 2012, dbmodel.FORD).save()
    model(u"Mustang", 2012, dbmodel.FORD).save()

    model(u"Escape", 2012, dbmodel.FORD, dbmodel.TRUCKS).save()
    model(u"F-150", 2012, dbmodel.FORD, dbmodel.TRUCKS).save()
    model(u"F-250", 2012, dbmodel.FORD, dbmodel.TRUCKS).save()
    model(u"F-350", 2012, dbmodel.FORD, dbmodel.TRUCKS).save()

    model(u"MKX", 2012, dbmodel.LINCOLN).save()
    model(u"Zephyr", 2012, dbmodel.LINCOLN).save()
    model(u"MKZ", 2012, dbmodel.LINCOLN).save()
    model(u"MKT", 2012, dbmodel.LINCOLN).save()
    sample_dealerInfo()
    conn.close()
