from django.db import models

# —————————————————————————————————————————————
#  Admin-configurable settings (durasi sesi, dsb)
# —————————————————————————————————————————————
class AdminConfig(models.Model):
    key   = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.key} = {self.value}"

    @classmethod
    def get_duration(cls):
        # contoh: durasi sesi default dalam menit
        val = cls.objects.filter(key="session_duration").first()
        return int(val.value) if val else 5  # default 5 menit

# —————————————————————————————————————————————
#  Desain Kolase & Slot
# —————————————————————————————————————————————
class CollageDesign(models.Model):
    name          = models.CharField(max_length=100)
    canvas_width  = models.PositiveIntegerField(help_text="Lebar canvas (px)")
    canvas_height = models.PositiveIntegerField(help_text="Tinggi canvas (px)")
    preview_image = models.ImageField(upload_to="collages/previews/")
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CollageSlot(models.Model):
    design      = models.ForeignKey(CollageDesign, on_delete=models.CASCADE, related_name="slots")
    order       = models.PositiveSmallIntegerField(help_text="Urutan slot")
    x           = models.IntegerField(help_text="Posisi X (px)")
    y           = models.IntegerField(help_text="Posisi Y (px)")
    width       = models.PositiveIntegerField(help_text="Lebar slot (px)")
    height      = models.PositiveIntegerField(help_text="Tinggi slot (px)")
    rotation    = models.IntegerField(default=0, help_text="Rotation angle (°)")

    class Meta:
        ordering = ["design", "order"]
        unique_together = [("design", "order")]

# —————————————————————————————————————————————
#  Filter Foto
# —————————————————————————————————————————————
class Filter(models.Model):
    name        = models.CharField(max_length=50)
    code        = models.CharField(max_length=100, help_text="Identifier untuk PIL/opencv")
    created_at  = models.DateTimeField(auto_now_add=True)