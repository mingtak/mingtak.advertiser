from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
#from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget, AutocompleteFieldWidget
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from mingtak.advertiser import MessageFactory as _

from mingtak.paymentmethod import payment

# Interface class; used to define content-type schema.

class IAdvertiser(form.Schema, IImageScaleTraversable):
    """
    Advertiser content type
    """
    logoImage = NamedBlogImage(
        title=_(u"Logo"),
        description=-(u"Advertiser logo image"),
        required=True,
    )

    webSite = Schema.URI(
        title=_(u"Website"),
        description=-(u"Advertiser website url, must include http://"),
        required=True,
    )
 
#    form.widget(allowedPayment=AutocompleteMultiFieldWidget)
    allowedPayment = RelationList(
        title=_(u"Allowed payment method"),
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=payment.IPayment.__identifier__,
            ),
        ),
        required=True,
    )


class Advertiser(Container):
    grok.implements(IAdvertiser)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IAdvertiser)
    grok.require('zope2.View')
    # grok.name('view')