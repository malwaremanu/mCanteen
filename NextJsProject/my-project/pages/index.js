// Konsta UI components
import {
  Page,
  Navbar,
  Block,
  Button,
  List,
  ListItem,
  Link,
  BlockTitle,
} from 'konsta/react';

export default function Home() {
  return (
    <Page>
      <Navbar title="mCanteen" />

      <Block strong>
        <p>
          Version 1.0
        </p>
      </Block>
      <BlockTitle>Simple Links List</BlockTitle>
      <List>
        <ListItem title="Link 1" link />
        <ListItem title="Link 2" link />
        <ListItem title="Link 3" link />
      </List>

      <List>
        <ListItem href="/aboutus/" title="About" />
        <ListItem href="/form/" title="Form" />
      </List>

      <Block strong className="flex space-x-4">
        <Button>Button 1</Button>
        <Button>Button 2</Button>
      </Block>
    </Page>
  );
}