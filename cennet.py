import os
import time
from rich.console import Console
from rich.table import Table

console = Console()

def sgy_selam():
    # Giriş Selamı
    os.system('termux-tts-speak -l tr "Selâmün Aleyküm"')
    time.sleep(1)
    os.system('termux-tts-speak -l tr "Aleyküm Selâm Sadık Hocam. Murat Çeşme karargahı hazır."')

def ana_panel():
    os.system('clear')
    table = Table(title="🌟 SGY UNIVERSAL MASTER - CENNET 🌟")
    table.add_column("Bölge", style="cyan")
    table.add_column("Durum", style="magenta")
    table.add_column("Güç/Merhamet", style="green")
    
    # Senin vizyonuna göre güncellendi
    table.add_row("Murat Çeşme (Merkez)", "DİK DURUŞ", "Maksimum")
    table.add_row("Ruhullah Lab", "Entegre", "Aktif")
    table.add_row("Dünya Haritası", "Aynalanıyor", "Hazır")
    
    console.print(table)
    print("\n[bold]Hassas evrensel doğru duruş ve güç devrede.[/bold]")

if __name__ == "__main__":
    sgy_selam()
    ana_panel()
