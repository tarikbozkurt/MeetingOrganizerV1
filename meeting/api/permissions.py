from rest_framework.permissions import BasePermission

#custom class eklemek için custom class oluşturuyoruz.


class IsOwner(BasePermission):
    """
    has_permission kuralsız koşulsuz direkt çalışır. Bu sebeple
    öncelikli olarak bir oturum kontrolü sağlayıp herhangi bir işlem
    yapmasına mani olabiliriz.

    has_object_permission belirlenen kurallar doğrultusunda çalışır.
    """
    #kullanıcı giriş yapmadan tetiklenir.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    message = "Bu objenin sahibi siz olmalısınız !"
    #Inherit aldığımız için fonksiyonu çektik.
    # BasePermission bilgilerini override edeceğiz..
    #kullanıcı giriş yaptıktan sonra tetiklenir
    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user) or request.user.is_superuser

