import os
import time
from rich.console import Console
from rich.table import Table

console = Console()

def adn_selami():
    # En derinden gelen selâm
    os.system('termux-tts-speak -l tr "Selâmün Aleyküm Sadık Hocam. Cennet-i Adn kapıları, doğru duruşunuz ve Ilgaz Efe mirası için aralanıyor."')

def cennet_tabakalari():
    os.system('clear')
    
    # Manevi ve Yüce Tabakalar Tablosu
    table = Table(title="✨ CENNET-İ ADN: EBEDİ SAADET VE REFAH MAKAMI ✨", border_style="bold yellow")
    
    table.add_column("Makam / Tabaka", style="cyan", justify="center")
    table.add_column("Özellik", style="magenta")
    table.add_column("SGY Master Vizyonu", style="green")

    table.add_row("ADN", "Ebedi İkametgâh", "Ilgaz Efe ve Soyunun Mirası")
    table.add_row("FİRDEVS", "Yüce Bahçeler", "Ruhullah Lab Bilgi Hazinesi")
    table.add_row("NAİM", "Nimet ve Huzur", "Hassas Maddiyat ve Güç")
    table.add_row("ME'VA", "Sığınak / Durak", "Murat Çeşme Karargahı")
    
    console.print(table)
    
    # Manevi Tasvir Notu
    console.print("\n[italic yellow]“Yeşil zeberced, kırmızı yakut ve inciyle inşa edilen o yüce âlem...”[/italic yellow]")
    console.print("\n[bold red]DURUŞ: DİK | GÜÇ: MANEVİ | MİRAS: EBEDİ[/bold red]")

if __name__ == "__main__":
    adn_selami()
    cennet_tabakalari()
