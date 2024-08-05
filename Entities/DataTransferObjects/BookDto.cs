using System.Reflection.Metadata.Ecma335;
using System.Text;

namespace Entities.DataTransferObjects
{
    public record BookDto()
    {
        public int Id { get; set; }
        public String Title { get; set; }
        public int price { get; set; }

    }

}
